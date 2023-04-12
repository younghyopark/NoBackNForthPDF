# NoBackNForthPDF

## Motivation
I spend a lot of time reading research papers in PDF, and I find it frustrating to constantly flip back and forth between pages to check the reference, figures, and equations. So, I decided to build a PDF viewer that makes it easier to navigate through papers and view citation information without scrolling back and forth all the time.

You can **hover over citations** to view reference information without having to go all the way back to the reference page. You can also do this for **figures and equations** as well. Just hover your mouse over `[xx]`, `Figure xx` and `Equation xx`, boom, you have the information you want with a nice yet non-intrusive popup. No need to wander around the whole paper finding the reference. You can also copy Bibtex citations to your clipboard with one click, making it easier to manage your references.

I hope this PDF viewer will make your research experience more efficient and enjoyable!

## To-Do

Nothing's been implemented yet. 

- [x] Render the PDF somehow
- [ ] Make it scrollable through pages
- [ ] Make the GUI user-friendly
- [ ] Draw a box around active hyperlinks 
- [ ] Make it show citation information when mouse hovers over the box 
- [ ] and more things ... 

## Install

```
pip install PyMuPDF PyQt6 crossrefapi
python main.py
```

and it will work. maybe..
