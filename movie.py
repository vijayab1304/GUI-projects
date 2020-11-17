import imdb
from tkinter import *


def search():
    root2 = Toplevel()
    root2.geometry('890x600+200+50')
    root2.title('Movie Information')
    root2.config(bg='#B39266')
    backpic = PhotoImage(file='toppic.png')
    backpicLabel = Label(root2, image=backpic).place(x=0,y=0)

    titleLabel = Label(root2, text='Title', font=('cooper black', 30, 'bold'), bg='#B39266', fg='white')
    titleLabel.place(x=60,y=30)

    titlenameLabel = Label(root2, font=('algerian', 20, 'bold'), bg='#B39266', fg='white')
    titlenameLabel.place(x=300, y=30)

    directorLabel = Label(root2, text='Director', font=('cooper black', 30, 'bold'), bg='#B39266', fg='white')
    directorLabel.place(x=60, y=100)

    directornameLabel = Label(root2, font=('algerian', 20, 'bold'), bg='#B39266', fg='white')
    directornameLabel.place(x=300, y=100)

    yearLabel = Label(root2, text='Year', font=('cooper black', 30, 'bold'), bg='#B39266', fg='white')
    yearLabel.place(x=60, y=170)

    yearnameLabel = Label(root2, font=('algerian', 20, 'bold'), bg='#B39266', fg='white')
    yearnameLabel.place(x=300, y=170)

    runtimeLabel = Label(root2, text='Runtime', font=('cooper black', 30, 'bold'), bg='#B39266', fg='white')
    runtimeLabel.place(x=60, y=240)

    runtimenameLabel = Label(root2, font=('algerian', 20, 'bold'), bg='#B39266', fg='white')
    runtimenameLabel.place(x=300, y=240)

    genreLabel = Label(root2, text='Genre', font=('cooper black', 30, 'bold'), bg='#B39266', fg='white')
    genreLabel.place(x=60, y=310)

    genrenameLabel = Label(root2, font=('algerian', 20, 'bold'), bg='#B39266', fg='white')
    genrenameLabel.place(x=300, y=310)

    ratingLabel = Label(root2, text='Rating', font=('cooper black', 30, 'bold'), bg='#B39266', fg='white')
    ratingLabel.place(x=60, y=380)

    ratingnameLabel = Label(root2, font=('algerian', 20, 'bold'), bg='#B39266', fg='white')
    ratingnameLabel.place(x=300, y=380)

    castLabel = Label(root2, text='Cast', font=('cooper black', 30, 'bold'), bg='#B39266', fg='white')
    castLabel.place(x=60, y=450)

    castnameLabel = Label(root2, font=('algerian', 20, 'bold'), wraplength=615, bg='#B39266', fg='white', justify=LEFT)
    castnameLabel.place(x=300, y=450)

    hr = imdb.IMDb()
    movie_name = movieEntry.get()
    movies = hr.search_movie(str(movie_name))

    index = movies[0].getID()
    movie = hr.get_movie(index)
    title = movie['title']

    titlenameLabel.config(text=title)

    year = movie['year']

    yearnameLabel.config(text=year)

    rating = movie['rating']

    ratingnameLabel.config(text=rating)

    genre = movie['genres']

    genrenameLabel.config(text=genre)

    for director in movie['directors']:
        directornameLabel.config(text=director)

    for runtime in movie['runtimes']:
        hours = int(runtime) // 60
        rem = int(runtime) % 60
        runtimenameLabel.config(text=f"{hours} hours {rem} minutes")

    cast = movie['cast']
    list_of_cast = ','.join(map(str, cast))
    castlist = list_of_cast.split(',')
    listitem = castlist[:10]
    strr = ''
    for i in listitem:

        if i == listitem[9]:
            strr = strr + i + ' '
        else:
            strr = strr + i + ',' + ' '

    castnameLabel.config(text=f'{strr}')

    root2.mainloop()























root = Tk()
root.geometry('1057x650+100+40')

root.title('Movie Description')
root.config(bg='#B39266')

bgpic = PhotoImage(file='pic.png')
bgLabel = Label(root, image=bgpic).place(x=0, y=0)

movieLabel = Label(root, text='MOVIE NAME:', font=('algerian', 30, 'bold'), bg='#DEDCDD', fg='gray20')
movieLabel.place(x=200, y=570)

movieEntry = Entry(root,font=('FELIX TITLING',20,'bold'),bd=5,relief=GROOVE,justify=CENTER,bg='#D9D7D9')
movieEntry.place(x=490,y=575)

moviesearchButton = Button(root,text='SEARCH',font=('FELIX TITLING',20,'bold'),bd=5,relief=GROOVE,bg='#D9D7D9',command=search)
moviesearchButton.place(x=880,y=565)













root.mainloop()