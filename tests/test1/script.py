from collator import collate

coll1 = collate(inputs=["a", "b"], outputs=["file.txt", "folder/file2.jpg"])
coll2 = collate(inputs=["d"], outputs=["file.txt"])

c = 7


@coll1
def run(a: int, b: int, c: int) -> int:
    output = a + b + c
    with open("file.txt", "w") as f:
        f.write(output)


@coll2
def run2(d: str) -> str:
    with open("file.txt", "w") as f:
        f.write(d)
