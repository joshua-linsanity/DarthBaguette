" MAPPINGS
" Treat wrapped line as true line (movement keys)
nnoremap j gj
nnoremap k gk

" Horizontal scroll
map <C-L> 5zl " Scroll 5 characters to the right
map <C-H> 5zh " Scroll 5 characters to the left

" Switch between tabs
nnoremap <C-S-Tab> :tabprevious<CR>
nnoremap <C-Tab> :tabnext<CR>
nnoremap <C-j> :tabprevious<CR>
nnoremap <C-k> :tabnext<CR>
tnoremap <C-e> <C-\><C-n><Return>

" GENERAL SETTINGS
" Highlighting
syntax on
nnoremap ,<space> :nohlsearch<CR>

" Tab
set tabstop=4
set softtabstop=4
set expandtab
set shiftwidth=4

" Highlight search results
set incsearch
set hlsearch

" Line numbering
set number

" No word wrap
set nowrap

" Stop annoying bell sounds
set belloff=all

" Use utf-8 encoding
set encoding=utf-8

" _vimrc - Links to the vimrc in the vimfiles directory
runtime vimrc

" PLUGINS
" New plugins (run :so % to source $MYVIMRC)
call plug#begin('$HOME/vimfiles/autoload')
Plug 'lervag/vimtex'
Plug 'nvim-tree/nvim-tree.lua'
Plug 'arcticicestudio/nord-vim'
call plug#end()

" Plugin keymaps
nnoremap <C-n> :NERDTree<CR>
lua require'nvim-tree'.setup {}
let g:python3_host_prog='C:/Users/foo/Envs/neovim3/Scripts/python.exe'
let g:python_host_prog='C:/Users/foo/Envs/neovim/Scripts/python.exe'

" Nvim-tree keymaps
nnoremap <C-n> :NvimTreeToggle<CR>
nnoremap <C-e> :NvimTreeFindFile<CR>
nnoremap <C-c> :NvimTreeClose<CR>

" BUILD SYSTEMS
" Java - F9 to compile, F10/F11 to cycle through errors
autocmd Filetype java set makeprg=javac\ %
set errorformat=%A%f:%l:\ %m,%-Z%p^,%-C%.%#
map <F9> :make<Return>:copen<Return>
map <F10> :cprevious<Return>
map <F11> :cnext<Return>

" Python - F12 to run
" nnoremap <buffer> <F12> :w <bar> !python %<CR>
autocmd Filetype python nnoremap <buffer> <F12> :w<CR>:vert ter python "%"<CR>
" autocmd FileType python map <buffer> <F12> :w<CR>:exec '!python' shellescape(@%, 1)<CR>
" autocmd FileType python imap <buffer> <F12> <esc>:w<CR>:exec '!python' shellescape(@%, 1)<CR>

