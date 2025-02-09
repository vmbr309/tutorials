# dotfiles
```sh
#### symbolic link
cd (path-to-destination-directory)
ln -s (path-to-origin)

#### extract brewfile
cd (path-to-directory) && brew bundle dump --force && git add . && git commit -m "update" && git push

#### Apply brewfile
brew bundle --file (path-to-file)

#### Git
git clone (url)
git add (file names)
git commit -m "(committed message)" (file names)
git push -u origin main 
git remote add origin main (url)( https://tokenhere@github.com/user_name/repo_name.git)
```