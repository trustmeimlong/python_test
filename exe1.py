def main():
    count = int(input("Nhập số lượng sinh viên: "))
    students = []
    for i in range(1, count + 1):
        print(f"\n--- Sinh viên {i} ---")
        student = {
            "id": input("Mã sinh viên: "),
            "name": input("Họ tên: "),
            "score": float(input("Điểm Python: ")),
        }
        students.append(student)
    print("\n--- Danh sách sinh viên ---")
    for student in students:
        print(f"{student['id']} - {student['name']} - {student['score']}")
    best = students[0]
    for student in students:
        if student["score"] > best["score"]:
            best = student
    print("\n--- Sinh viên có điểm cao nhất ---")
    print(f"{best['id']} - {best['name']} - {best['score']}")
    total = 0
    for student in students:
        total += student["score"]
    average = total / count
    print(f"\nĐiểm trung bình: {average:.2f}")
    print("\n--- Sinh viên đạt (điểm >= 5) ---")
    for student in students:
        if student["score"] >= 5:
            print(f"{student['id']} - {student['name']} - {student['score']}")

if __name__ == '__main__':
    main()