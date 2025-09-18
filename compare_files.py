



def compare_files(file1_path, file2_path, ignore_title=False, ignore_date=False, show_line_diff=True):
    with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    differences = []
    diff_line_count = 0

    # Compare title (line 0)
    if not ignore_title:
        if lines1[0].strip() != lines2[0].strip():
            differences.append("Title is different.")

    # Compare date (line 1)
    if not ignore_date:
        if len(lines1) > 1 and len(lines2) > 1:
            if lines1[1].strip() != lines2[1].strip():
                differences.append("Date is different.")
        else:
            differences.append("Date line missing in one of the files.")

    # Compare text content (from line 2 onward)
    text1 = lines1[2:] if len(lines1) > 2 else []
    text2 = lines2[2:] if len(lines2) > 2 else []

    if text1 != text2:
        differences.append("Text content is different.")
        if show_line_diff:
            max_len = max(len(text1), len(text2))
            print("\nLine-by-line differences:")
            for i in range(max_len):
                line1 = text1[i].strip() if i < len(text1) else "<missing>"
                line2 = text2[i].strip() if i < len(text2) else "<missing>"
                if line1 != line2:
                    diff_line_count += 1
                    print(f"Line {i+3}:")
                    print(f"  File1: {line1}")
                    print(f"  File2: {line2}")

    # Final result
    if not differences:
        print("Files are similar.")
    else:
        print("\nFiles are different:")
        for diff in differences:
            print(f"- {diff}")
        if show_line_diff:
            print(f"\nTotal number of different lines: {diff_line_count}")

# Example usage:
compare_files('file1.txt', 'file2.txt', ignore_title=False, ignore_date=False, show_line_diff=True)



# Example usage:
compare_files('files/WhoAreYou_NF70_06047_08132025.dat', 'files/WhoAreYou_NF70_06047_08202025.dat', ignore_title=True, ignore_date=False, show_line_diff=True)
