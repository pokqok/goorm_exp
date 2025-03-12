import os


class Book:

    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False


class Ebook(Book):

    def __init__(self, title, author, file_size, is_borrowed=False):
        super().__init__(title, author, is_borrowed)
        self.file_size = file_size

    def download(self):
        print(f"{self.title} 다운로드 완료! ({self.file_size}MB)")


class Library:

    def __init__(self, filename="books.txt"):
        # 현재 스크립트의 경로를 기준으로 파일 경로 설정
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.books = []
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")
            
                if len(data) == 3:  # 종이책
                    title, author, is_borrowed = data
                    book = Book(title, author, is_borrowed == 'True')  # 대출 여부 처리
                    self.books.append(book)

                elif len(data) == 4:  # 전자책
                    title, author, is_borrowed, file_size = data
                    # file_size가 없을 경우, default 값(0) 처리
                    file_size = int(file_size) if file_size else 0
                    book = Ebook(title, author, file_size, is_borrowed == 'True')  # 대출 여부 처리
                    self.books.append(book)


    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for book in self.books:
                if isinstance(book, Ebook):
                    file.write(
                        f"{book.title},{book.author},{book.is_borrowed},{book.file_size}\n"
                    )
                else:
                    file.write(f"{book.title},{book.author},{book.is_borrowed}\n")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()  # 책이 추가될 때마다 파일에 저장

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if isinstance(book, Ebook):
                    raise ValueError("⚠️ 전자책은 다운로드로 가세요")
                if book.is_borrowed:
                    raise ValueError("⚠️ 이미 대출된 책입니다!")  # 예외로 함수 종료
                book.borrow()
                print(f"{title}을(를) 빌렸습니다.")
                self.save_books()  # 대출 시 파일에 저장
                return  # 성공적으로 빌렸다면 함수 종료

        raise ValueError(
            "⚠️ 해당 책이 없습니다."
        )  # 루프를 다 돌고도 못 찾으면 예외 발생

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"{title}을(를) 반납했습니다.")
                self.save_books()  # 반납 시 파일에 저장
                return  # 성공적으로 반납했다면 함수 종료

        raise ValueError(
            "⚠️ 해당 책이 없습니다."
        )  # 루프를 다 돌고도 못 찾으면 예외 발생

    def show_books(self):
        '''리스트 컴프리헨션을 사용하여 출력'''
        # 종이책은 대출 여부 표시, 용량 미표시
        paper_books = [f" {book.title} ({'대출 중' if book.is_borrowed else '대출 가능'})" for book in self.books if not isinstance(book, Ebook)]
    
        # 전자책은 대출 여부 표시 없이 용량만 표시
        ebooks = [f" {book.title} - {book.file_size}MB" for book in self.books if isinstance(book, Ebook)]

        print("\n 현재 도서 목록:")
    
        # 종이책이 있을 경우 출력
        if paper_books:
            print("\n 종이책 목록:")
            print("\n".join(paper_books))
    
        # 전자책이 있을 경우 출력
        if ebooks:
            print("\n 전자책 목록:")
            print("\n".join(ebooks))
    
        # 종이책과 전자책이 모두 없을 경우
        if not paper_books and not ebooks:
            print("도서관이 비어 있습니다.")


    def download_book(self, title):
        for book in self.books:
            if book.title == title:
                if isinstance(book, Ebook):  # book이 Ebook 클래스가 아니라면
                    book.download()
                else:
                    print("⚠️ 종이책은 다운로드할 수 없습니다!")
                return

        print("⚠️ 해당 책이 없습니다.")


# 실행 코드
library = Library()
while True:
    try:
        print("\n📚 도서 관리 시스템 📚")
        print("1. 종이책 추가")
        print("2. 전자책 추가")
        print("3. 책 대출")
        print("4. 책 반납")
        print("5. 전자책 다운로드")
        print("6. 책 목록 보기")
        print("7. 종료")

        num = input("선택: ")

        if num == "1":
            title = input("종이책 제목: ")
            author = input("저자: ")
            library.add_book(Book(title, author))

        elif num == "2":
            title = input("전자책 제목: ")
            author = input("저자: ")
            file_size = int(input("파일 크기(MB): "))
            library.add_book(Ebook(title, author, file_size))

        elif num == "3":
            title = input("대출할 책 제목: ")
            library.borrow_book(title)

        elif num == "4":
            title = input("반납할 책 제목: ")
            library.return_book(title)

        elif num == "5":
            title = input("다운로드할 전자책 제목: ")
            library.download_book(title)

        elif num == "6":
            library.show_books()

        elif num == "7":
            print("도서 관리 시스템을 종료합니다.")
            break

        else:
            print("올바르게 입력해주세요")

    except ValueError as e:
            print(e)  # 오류 메시지 출력
            continue  # 초기 화면으로 돌아가도록 continue

    except Exception as e:
            print(f"알 수 없는 오류: {e}")
            break  # 예기치 않은 오류는 종료