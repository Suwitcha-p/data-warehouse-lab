import duckdb

# เชื่อมต่อกับไฟล์ฐานข้อมูล dev.duckdb ในโฟลเดอร์ปัจจุบัน
conn = duckdb.connect('dev.duckdb')

# ดึงรายชื่อตารางทั้งหมด
tables = conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'main' ORDER BY table_name").fetchall()

# แสดงผลลัพธ์ออกทางหน้าจอ
print(f"🎉 พบตารางในฐานข้อมูลทั้งหมด: {len(tables)} ตาราง")
print("-" * 40)

for i, table in enumerate(tables, 1):
    print(f"{i:2d}. {table[0]}")

print("-" * 40)

conn.close()
