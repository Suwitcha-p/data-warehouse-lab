# data-warehouse-lab
study lab data-warehouse-lab
##Basic git command 
command 

- `git clone Get the course repo`	
- `git add + git commit	Save your work`	
- `git push	Back it up to GitHub`	
- `git checkout -b	Try something without breaking main`	
- `git log --onelineSee what you've done`	

__________________________________________________________________________

---
## **โครงสร้างมาตรฐาน (Project Structure) ที่ dbt สร้างขึ้น**

เป็นระบบตามแนวทางของ Analytics Engineering โดยแต่ละโฟลเดอร์มีหน้าที่แตกต่างกันดังนี้:

    1. seeds/ (ตารางข้อมูลอ้างอิง)
ใช้สำหรับเก็บไฟล์ข้อมูลขนาดเล็กเช่นตารางอ้างอิง ตารางรหัสสินค้า (ที่เป็นไฟล์ .csv) เพื่อให้ dbt นำไปสร้างเป็นตารางในฐานข้อมูลโดยอัตโนมัติ

เหมาะสำหรับ: ข้อมูลที่ไม่ได้อยู่ในระบบฐานข้อมูลหลัก แต่จำเป็นต้องนำมาใช้ JOIN หรืออ้างอิง เช่น ตารางรายชื่อประเทศ, รหัสไปรษณีย์, หรือคำอธิบายสถานะออเดอร์

วิธีใช้: นำไฟล์ CSV ไปวาง แล้วรันคำสั่ง dbt seed ข้อมูลจะถูกอัปโหลดเข้าฐานข้อมูลทันที

    2. macros/ (โค้ดที่ใช้ซ้ำได้)    
คือโฟลเดอร์ที่เก็บ "ฟังก์ชัน" หรือชุดคำสั่ง SQL ที่เขียนขึ้นเองเพื่อใช้ซ้ำได้ทั้งโปรเจกต์

สมมุติต้องคำนวณภาษีมูลค่าเพิ่ม (VAT 7%) จากยอดขายบ่อยๆ แทนที่จะเขียน amount * 0.07 ทุกที่ ให้สร้างไฟล์ในโฟลเดอร์ macros/
```sql
-- ไฟล์: macros/calculate_tax.sql
{% macro calculate_tax(amount_column, tax_rate=0.07) %}
    ({{ amount_column }} * {{ tax_rate }})
{% endmacro %}
```

เมื่อสร้าง Macro เสร็จแล้ว คุณสามารถเรียกใช้ภายในโมเดล SQL ของคุณได้ง่ายๆ โดยใช้ไวยากรณ์ {{ ชื่อ_macro(...) }} ดังนี้:
```sql
-- ไฟล์: models/stg_orders.sql
with orders as (
    select * from {{ source('northwind', 'orders') }}
)

select
    order_id,
    order_amount,
    -- เรียกใช้ Macro มาคำนวณภาษี
    {{ calculate_tax('order_amount') }} as tax_amount,
   
    -- เรียกใช้ Macro โดยระบุอัตราภาษีพิเศษ (เช่น 10%)
    {{ calculate_tax('order_amount', tax_rate=0.10) }} as tax_amount_high_rate
from orders
```
