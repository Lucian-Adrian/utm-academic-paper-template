\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{utmabstract}[2026/04/30 UTM conference abstract class]

\LoadClass[12pt,a4paper]{article}
\RequirePackage[a4paper,top=2cm,bottom=2cm,left=2.5cm,right=2cm,headsep=1cm,footskip=1.25cm]{geometry}
\RequirePackage{iftex}
\ifPDFTeX
  \RequirePackage[T1]{fontenc}
  \RequirePackage[utf8]{inputenc}
  \RequirePackage{mathptmx}
\else
  \RequirePackage{fontspec}
  \IfFontExistsTF{Times New Roman}{\setmainfont{Times New Roman}}{\setmainfont{Liberation Serif}}
\fi
\RequirePackage{graphicx}
\RequirePackage{setspace}

\setstretch{1}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\pagestyle{empty}

\newcommand{\UTMAbstractTitle}{}
\newcommand{\UTMAbstractAuthors}{}
\newcommand{\UTMAbstractAffiliations}{}
\newcommand{\UTMAbstractCorresponding}{}
\newcommand{\UTMAbstractSupervisor}{}
\newcommand{\UTMLogoPath}{../../shared/assets/UTM_Logo.png}
\newif\ifUTMShowLogo
\UTMShowLogofalse

\newcommand{\abstracttitle}[1]{\renewcommand{\UTMAbstractTitle}{#1}}
\newcommand{\abstractauthors}[1]{\renewcommand{\UTMAbstractAuthors}{#1}}
\newcommand{\abstractaffiliations}[1]{\renewcommand{\UTMAbstractAffiliations}{#1}}
\newcommand{\abstractcorresponding}[1]{\renewcommand{\UTMAbstractCorresponding}{#1}}
\newcommand{\abstractsupervisor}[1]{\renewcommand{\UTMAbstractSupervisor}{#1}}
\newcommand{\utmlogo}[1]{\renewcommand{\UTMLogoPath}{#1}}

\newcommand{\makeutmabstracttitle}{%
  \begin{center}
  \ifUTMShowLogo
    \includegraphics[height=1.8cm]{\UTMLogoPath}\par\vspace{6pt}
  \fi
  {\bfseries\fontsize{14pt}{16pt}\selectfont\MakeUppercase{\UTMAbstractTitle}\par}
  \vspace{12pt}
  {\bfseries\fontsize{12pt}{14pt}\selectfont\UTMAbstractAuthors\par}
  \vspace{12pt}
  {\itshape\fontsize{10pt}{12pt}\selectfont\UTMAbstractAffiliations\par}
  \vspace{12pt}
  {\fontsize{10pt}{12pt}\selectfont\UTMAbstractCorresponding\par}
  \vspace{12pt}
  {\fontsize{10pt}{12pt}\selectfont\UTMAbstractSupervisor\par}
  \end{center}
  \vspace{12pt}
}

\newenvironment{rezumat}
  {\noindent\textbf{\textit{Rezumat.}}\ \itshape\fontsize{12pt}{14pt}\selectfont}
  {\par\vspace{12pt}}

\newcommand{\cuvintecheie}[1]{%
  \noindent\textbf{\textit{Cuvinte cheie:}}\ \textit{#1}\par
}
