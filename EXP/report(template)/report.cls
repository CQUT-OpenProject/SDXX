\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{report}[2026/09/12 CQUT experimental report template]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexart}}
\ProcessOptions\relax
\LoadClass[a4paper,UTF8,zihao=-4,fontset=none,oneside]{ctexart}

\RequirePackage{fontspec}
\RequirePackage{xeCJK}
\RequirePackage[a4paper,left=25mm,right=18mm,top=20mm,bottom=20mm,headheight=0pt,headsep=0pt,footskip=10mm]{geometry}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{setspace}
\RequirePackage{indentfirst}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{xcolor}
\RequirePackage{listings}
\RequirePackage{hyperref}

\setCJKmainfont[BoldFont={Songti SC Bold}]{Songti SC}
\setCJKsansfont[BoldFont={Heiti SC Medium}]{Heiti SC}
\setCJKmonofont{STFangsong}
\newCJKfontfamily\cqutheiti[BoldFont={Hiragino Sans GB W6}]{Hiragino Sans GB W3}
\newCJKfontfamily\cqutsongti[BoldFont={Songti SC Bold}]{Songti SC}
\newCJKfontfamily\cqutfangsong{STFangsong}
\setmainfont{Times New Roman}
\setmonofont{Menlo}

\hypersetup{hidelinks,unicode=true,hypertexnames=false}
\setlength{\parindent}{2em}
\setlength{\parskip}{0pt}
\setstretch{1.22}

\def\cqut@university{重庆理工大学}
\def\cqut@coursetitle{深度学习}
\def\cqut@college{计算机科学与工程学院}
\def\cqut@studentid{}
\def\cqut@authorname{}
\def\cqut@advisor{}
\def\cqut@date{}
\def\cqut@expnum{1}
\def\cqut@exptitle{环境搭建与 python 初步应用}

\newcommand{\university}[1]{\def\cqut@university{#1}}
\newcommand{\coursetitle}[1]{\def\cqut@coursetitle{#1}}
\newcommand{\college}[1]{\def\cqut@college{#1}}
\newcommand{\studentid}[1]{\def\cqut@studentid{#1}}
\newcommand{\authorname}[1]{\def\cqut@authorname{#1}}
\newcommand{\advisor}[1]{\def\cqut@advisor{#1}}
\newcommand{\reportdate}[1]{\def\cqut@date{#1}}
\newcommand{\expnum}[1]{\def\cqut@expnum{#1}}
\newcommand{\exptitle}[1]{\def\cqut@exptitle{#1}}

\fancypagestyle{reportstyle}{%
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[C]{\fontsize{9pt}{11pt}\selectfont\thepage/\pageref{LastPage}}
}
\pagestyle{reportstyle}

\newcommand{\cqut@infoline}[2]{%
  \makebox[5.5em][s]{#1} & \underline{\makebox[185pt][c]{#2}} \\
}

\newcommand{\makecover}{%
  \thispagestyle{reportstyle}
  \begin{center}
    \vspace*{-5pt}
    \includegraphics[width=285pt,trim=0 0 597 0,clip]{assets/cqut-logo-horizontal.png}\par
    \vspace{85pt}
    {\fontsize{26pt}{34pt}\selectfont\cqutsongti\bfseries \cqut@coursetitle\par}
    \vspace{95pt}
    {\fontsize{15pt}{22pt}\selectfont\cqutsongti
      \begin{tabular}{r@{\hspace{1.2em}}l}
        \cqut@infoline{学\hfill 院}{\cqut@college} \\[1.4em]
        \cqut@infoline{学\hfill 号}{\cqut@studentid} \\[1.4em]
        \cqut@infoline{姓\hfill 名}{\cqut@authorname} \\[1.4em]
        \cqut@infoline{指\hfill 导\hfill 教\hfill 师}{\cqut@advisor} \\[1.4em]
        \cqut@infoline{时\hfill 间}{\cqut@date} \\
      \end{tabular}
    }
  \end{center}
  \vfill
  \clearpage
}

\newcommand{\makereportheader}{%
  \begin{center}
    {\cqutheiti\zihao{3}\textbf{实验~\cqut@expnum~ \cqut@exptitle}\par}
  \end{center}
  \vspace{2mm}
}

\newcommand{\sectheader}[1]{%
  \par\vspace{1.8ex}%
  {\noindent\cqutheiti\zihao{4}\textbf{#1}}%
  \par\vspace{1.2ex}%
}

\newcommand{\sectdivider}{%
  \par\vspace{2.4ex}%
  \noindent{\color{black!25}\rule{\linewidth}{0.4pt}}%
  \par\vspace{2.4ex}%
}

\newcommand{\exlabel}[1]{\noindent\hspace{2em}\textbf{#1}\quad}

\newcommand{\resultspace}[1][3.2cm]{\par\vspace{#1}}

\lstdefinestyle{cqutpython}{
  language=Python,
  basicstyle={\cqutfangsong\fontsize{9.5pt}{12pt}\selectfont},
  keywordstyle=\bfseries\color{black},
  commentstyle=\color[gray]{0.35},
  stringstyle=\color[gray]{0.2},
  numbers=none,
  showspaces=false,
  showstringspaces=false,
  breaklines=true,
  breakatwhitespace=true,
  tabsize=4,
  xleftmargin=0pt,
  columns=flexible,
  keepspaces=true,
  aboveskip=0.6ex,
  belowskip=0.6ex,
  backgroundcolor=\color{white},
  frame=none
}

\lstdefinestyle{cqutoutput}{
  basicstyle={\cqutfangsong\fontsize{9.5pt}{12pt}\selectfont},
  numbers=none,
  showspaces=false,
  showstringspaces=false,
  breaklines=true,
  tabsize=4,
  xleftmargin=0pt,
  columns=flexible,
  keepspaces=true,
  aboveskip=0.6ex,
  belowskip=0.6ex,
  backgroundcolor=\color{white},
  frame=none
}

\lstset{style=cqutpython}

\endinput
