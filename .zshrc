# Path to your oh-my-zsh installation.
export ZSH=/Users/jerry/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="robbyrussell"
#ZSH_THEME='amuse'
# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

# User configuration

export PATH="/Users/jerry/anaconda/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin"
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_77.jdk/Contents/Home
export RUST_SRC_PATH=/usr/local/src/rust/src
export PATH=/Users/jerry/apache-maven-3.3.9/bin:$PATH
# export MANPATH="/usr/local/man:$MANPATH"
export PATH=/Users/jerry/Documents/ShanghaiTech/research/Rust/k-framework/k/bin:$PATH
# SML
export PATH=$PATH:/usr/local/smlnj/bin
source $ZSH/oh-my-zsh.sh
# rustup
export PATH=$HOME/.cargo/bin:$PATH
export http_proxy='http://localhost:8118'
export https_proxy='http://localhost:8118'
# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
eval $(thefuck --alias)
alias jn='jupyter notebook'
alias vi='vim'
alias pserver='python -m SimpleHTTPServer 8000'
alias -s txt=vi
alias hp='hexo clean && hexo deploy'
alias bs='browser-sync start --server --directory --files "*"'
alias cls='clear'
alias cb='cargo build'
alias cr='cargo run'
alias lr='/Users/jerry/Documents/coding/learn_rust'
alias cr='cargo run'
alias -s rs=rustc
alias github='/Users/jerry/Documents/coding/github'
alias -s md=typora
alias blog='/Users/jerry/hexo-theme-huxblog'
alias lrp='/Users/jerry/Documents/coding/learn_rust/practice'
alias -s py=python
alias -s k=kompile
alias -s jemdoc=jemdoc
alias diary='/Users/jerry/Documents/ShanghaiTech/Diary'
alias nd='python /Users/jerry/Documents/ShanghaiTech/Diary/generate.py'
alias typora='open -a typora'
alias sqlmap='python /Users/jerry/Documents/WebSecurity/sqlmap/sqlmap.py'
alias ro='rlwrap ocaml'
alias krust="/Users/jerry/Documents/ShanghaiTech/research/Rust/k-framework/Rust"
alias gb="git branch"
alias gc='git clone'
alias gp='git push origin master'
alias rustbook='/usr/local/share/doc/rust'
alias gm="git commit -m"
alias master="git checkout master"
alias gc="git checkout"
alias em='emacs'
alias cb='cargo build'
alias jemdoc='/Users/jerry/Documents/Coding/jemdoc/jemdoc.py'
alias ct='cargo test'
alias kc='kompile'
alias kr='krun'
alias cr='cargo run'
alias rm='trash'
alias sml='rlwrap /usr/local/smlnj/bin/sml'
alias zhangty='ssh zhangty@10.19.124.11'
alias ga='git add .'
alias pserver='python -m SimpleHTTPServer'
alias rust='/Users/jerry/Documents/ShanghaiTech/科研/Rust'
alias c11='/Users/jerry/Documents/ShanghaiTech/research/Rust/k-framework/K-Projects/c-semantics/semantics/c11'
alias coding='/Users/jerry/Documents/Coding'
export PYTHONPATH="/Users/jerry/.smt_solvers/python-bindings-2.7:${PYTHONPATH}"
export OPENSSL_INCLUDE_DIR="brew --prefix openssl"/include
export OPENSSL_LIB_DIR="brew --prefix openssl"/lib
export PATH="$HOME/.yarn/bin:$PATH"
export PATH="$PATH:/Users/jerry/Downloads/play"
PATH="/Users/jerry/perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="/Users/jerry/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/Users/jerry/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/Users/jerry/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/Users/jerry/perl5"; export PERL_MM_OPT;

