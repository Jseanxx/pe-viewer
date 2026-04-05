def main():
    print("파일 실행됨....")
    path = input("뷰어할 exe 경로를 입력하세요: ")

    with open(path, "rb") as f: #rb는 바이너리 모드로 읽겠다는 뜻.
        data = f.read()

    print(data[:2])             #MZ 출력
    raw = data[0x3C:0x40]
    e_lfanew_off = int.from_bytes(raw, "little")

    print(f"e_lfanew: 0x{e_lfanew_off:08X}")

    NT_Header = data[e_lfanew_off:e_lfanew_off+4]
    print(NT_Header)

if __name__ == "__main__":
    main()