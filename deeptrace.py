from core.exif_analyzer import extract_exif
from core.ext_redflag import analyze_text
from utils.formatter import print_section, print_result
from rich import print

def banner():
    print("""
[bold red]
██████╗ ███████╗███████╗██████╗ ████████╗██████╗  █████╗  ██████╗███████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
██║  ██║█████╗  █████╗  ██████╔╝   ██║   ██████╔╝███████║██║     █████╗
██║  ██║██╔══╝  ██╔══╝  ██╔═══╝    ██║   ██╔══██╗██╔══██║██║     ██╔══╝
██████╔╝███████╗███████╗██║        ██║   ██║  ██║██║  ██║╚██████╗███████╗
╚═════╝ ╚══════╝╚══════╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
[/bold red]
[bold yellow]DeepTrace – OSINT Image & Text Investigation Tool[/bold yellow]
    """)

def main():
    banner()

    print("1) Image Metadata Investigation (EXIF)")
    print("2) Text Linguistic Red-Flag Analyzer\n")

    choice = input("Choose option: ").strip()

    if choice == "1":
        path = input("Enter image path: ").strip()
        print_section("Image Investigation Result")
        data = extract_exif(path)
        print_result(data)

    elif choice == "2":
        text = input("Paste suspicious text:\n")
        print_section("Text Investigation Result")
        result = analyze_text(text)
        print_result(result)

    else:
        print("[red]Invalid option selected[/red]")

if __name__ == "__main__":
    main()
