\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{utmconf}[2026/04/29 UTM conference academic paper class]

\LoadClass[12pt,a4paper]{article}

\RequirePackage[a4paper,top=2cm,bottom=2cm,left=2.5cm,right=2cm,headsep=1cm,footskip=1.25cm]{geometry}
\RequirePackage{iftex}
\ifPDFTeX
  \RequirePackage[T1]{fontenc}
  \RequirePackage[utf8]{inputenc}
  \RequirePackage{mathptmx}
\else
  \RequirePackage{fontspec}
  \IfFontExistsTF{Times New Roman}
    {\setmainfont{Times New Roman}}
    {\setmainfont{Liberation Serif}}
\fi
\RequirePackage{graphicx}
\RequirePackage{amsmath}
\RequirePackage{array}
\RequirePackage{tabularx}
\RequirePackage{caption}
\RequirePackage{enumitem}
\RequirePackage{indentfirst}
\RequirePackage{setspace}
\RequirePackage{titlesec}
\RequirePackage{ragged2e}

\setstretch{1}
\setlength{\parindent}{1.25cm}
\setlength{\parskip}{0pt}
\AtBeginDocument{\fontsize{12pt}{14pt}\selectfont}

\titleformat{\section}
  {\normalfont\bfseries\fontsize{12pt}{14pt}\selectfont}
  {}
  {0pt}
  {}
\titlespacing*{\section}{0pt}{12pt}{0pt}

\titleformat{\subsection}
  {\normalfont\bfseries\fontsize{12pt}{14pt}\selectfont}
  {}
  {0pt}
  {}
\titlespacing*{\subsection}{0pt}{12pt}{0pt}

\setlist[itemize]{leftmargin=1.25cm,itemsep=0pt,topsep=0pt,parsep=0pt,partopsep=0pt}
\setlist[enumerate]{leftmargin=1.25cm,itemsep=0pt,topsep=0pt,parsep=0pt,partopsep=0pt}

\newenvironment{utmenumerate}
  {\begin{enumerate}[label=\alph*)]}
  {\end{enumerate}}

\newcommand{\UTMTitle}{}
\newcommand{\UTMAuthors}{}
\newcommand{\UTMAffiliations}{}
\newcommand{\UTMCorrespondingAuthor}{}
\newcommand{\UTMSupervisor}{}
\newcommand{\UTMLogoPath}{assets/UTM_Logo.png}
\newif\ifUTMShowLogo
\UTMShowLogofalse

\newcommand{\papertitle}[1]{\renewcommand{\UTMTitle}{#1}}
\newcommand{\paperauthors}[1]{\renewcommand{\UTMAuthors}{#1}}
\newcommand{\paperaffiliations}[1]{\renewcommand{\UTMAffiliations}{#1}}
\newcommand{\correspondingauthor}[1]{\renewcommand{\UTMCorrespondingAuthor}{#1}}
\newcommand{\scientificsupervisor}[1]{\renewcommand{\UTMSupervisor}{#1}}
\newcommand{\utmlogo}[1]{\renewcommand{\UTMLogoPath}{#1}}

\newcommand{\makeutmtitle}{%
  \begin{center}
  \ifUTMShowLogo
    \includegraphics[height=1.8cm]{\UTMLogoPath}\par\vspace{6pt}
  \fi
  {\bfseries\fontsize{14pt}{16pt}\selectfont\MakeUppercase{\UTMTitle}\par}
  \vspace{12pt}
  {\bfseries\fontsize{12pt}{14pt}\selectfont\UTMAuthors\par}
  \vspace{12pt}
  {\itshape\fontsize{10pt}{12pt}\selectfont\UTMAffiliations\par}
  \vspace{12pt}
  {\fontsize{10pt}{12pt}\selectfont\UTMCorrespondingAuthor\par}
  \vspace{12pt}
  {\fontsize{10pt}{12pt}\selectfont\UTMSupervisor\par}
  \end{center}
  \vspace{12pt}
}

\newenvironment{rezumat}
  {\noindent\textbf{\textit{Rezumat.}}\ \itshape}
  {\par\vspace{12pt}}

\newcommand{\cuvintecheie}[1]{%
  \noindent\textbf{\textit{Cuvinte cheie:}}\ \textit{#1}\par\vspace{12pt}
}

\newenvironment{abstracten}
  {\noindent\textbf{\textit{Abstract.}}\ \itshape}
  {\par\vspace{12pt}}

\newcommand{\keywords}[1]{%
  \noindent\textbf{\textit{Keywords:}}\ \textit{#1}\par\vspace{12pt}
}

\renewcommand{\tablename}{Tabelul}
\renewcommand{\figurename}{Figura}
\numberwithin{equation}{section}

\newcounter{utmtable}
\newcommand{\utmtablecaption}[1]{%
  \refstepcounter{utmtable}%
  \begin{flushright}
    \bfseries\fontsize{11pt}{13pt}\selectfont Tabelul \theutmtable
  \end{flushright}
  \begin{center}
    \bfseries\fontsize{11pt}{13pt}\selectfont #1
  \end{center}
  \vspace{-6pt}
}

\newcounter{utmfigure}
\newcommand{\utmfigurecaption}[1]{%
  \refstepcounter{utmfigure}%
  \begin{center}
    \bfseries\fontsize{11pt}{13pt}\selectfont Figura \theutmfigure. #1
  \end{center}
}

\captionsetup{font=small,labelfont=bf}
\captionsetup[figure]{justification=centering,singlelinecheck=true,position=bottom}
\captionsetup[table]{justification=raggedleft,singlelinecheck=false,position=top}

\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}
\renewcommand{\arraystretch}{1.15}

\pagestyle{plain}
