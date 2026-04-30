% #####
% Definition of the custom class "thesis":
% #####

\NeedsTeXFormat{LaTeX2e}

\ProvidesClass{thesis}[01/09/2021 LaTeX Thesis Template]

\LoadClass{report}


% #####
% Packages / Libs:
% #####

\RequirePackage{amsmath}

\RequirePackage[english]{babel}

\RequirePackage{caption}

\RequirePackage{enumerate}

\RequirePackage{enumitem}

\RequirePackage{eso-pic}

\RequirePackage{float}

\RequirePackage{graphicx}

\RequirePackage[utf8]{inputenc}

\RequirePackage[nopostdot]{glossaries}

\RequirePackage{indentfirst}

\RequirePackage{csquotes}

\RequirePackage{listings}

\RequirePackage{mathptmx}

\RequirePackage[fontsize=12pt]{scrextend}

\RequirePackage{setspace}

\RequirePackage{titlesec}

\RequirePackage{tocloft}

\RequirePackage[final]{pdfpages}

\RequirePackage{hyperref}

\RequirePackage[a4paper, 
				left=20mm, 
				right = 1cm, 
				top = 2cm, 
				bottom = 2cm]{geometry}

\RequirePackage[backend=biber, 
				style=numeric,
				sorting=none]{biblatex}



% #####
% New commands:
% #####

\newcommand{\showfigure}[4]{
	\begin{figure}[H] 
		\centering 
		\includegraphics[scale=#1]{#2} 
		\caption{#3}
		\label{fig:#4} 
	\end{figure}
	\vspace{-1.5em}
}

\addto\captionsenglish{
    \renewcommand{\figurename}
                 {\textbf{Figura}}
}

\setlength{\abovecaptionskip}{10pt} 
\setlength{\belowcaptionskip}{0pt}

\newcommand{\hitem}
           {\item[-]}



% #####
% Settings for text:
% #####

\setstretch{1.5}

\setlist{nolistsep}

\setlength{\parindent}{1.25cm}

\renewcommand{\arraystretch}{1.2}
\renewcommand*{\arraystretch}{1.2}

\lstset{breaklines=true}

\hypersetup{unicode=true}

\titleformat{\chapter}[block]
            {\centering \bfseries \large}
            {\thechapter}
            {5pt}
            {}
            
\titlespacing{\chapter}{0pt}{0pt}{0pt}

\titleformat{\section}
            {\bfseries \normalsize}
            {\thesection}
            {5pt}
            {}
            
\titlespacing{\section}{\parindent}{10pt}{0pt}
            
\titleformat*{\subsection}
            {\bfseries \normalsize}

\titlespacing{\subsection}{\parindent}{10pt}{0pt}

\titleformat*{\subsubsection}
            {\bfseries \normalsize}
            
\titlespacing{\subsubsection}{\parindent}{10pt}{0pt}

\addto\captionsenglish{
    \renewcommand{\contentsname}
                 {Table of contents}
}

\addto\captionsenglish{
    \renewcommand{\listfigurename}
                 {List of figures}
}

\addto\captionsenglish{
    \renewcommand{\listtablename}
                 {List of tables}
}

\addto\captionsenglish{
    \renewcommand{\glossaryname}
                 {Glossary}
}

\renewcommand{\addvspace}[1]{}

\renewcommand{\cftpartleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftchapleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}

\renewcommand{\cfttoctitlefont}{\hfill \large \bfseries}
\renewcommand{\cftloftitlefont}{\hfill \large \bfseries}
\renewcommand{\cftlottitlefont}{\hfill \large \bfseries}

\renewcommand{\cftaftertoctitle}{\hfill\hfill}
\renewcommand{\cftafterloftitle}{\hfill}
\renewcommand{\cftafterlottitle}{\hfill}

\setlength{\cftbeforetoctitleskip}{0pt}
\setlength{\cftbeforeloftitleskip}{0pt}
\setlength{\cftbeforelottitleskip}{0pt}

\setlength{\cftaftertoctitleskip}{0pt}
\setlength{\cftafterloftitleskip}{0pt}
\setlength{\cftafterlottitleskip}{0pt}

\setlength{\cftbeforechapskip}{0pt}


% #####
% Settings for tables and figures:
% #####

\DeclareCaptionLabelSeparator{dash}{ - }

\captionsetup[table]{
	labelsep=dash, 
	justification=raggedleft, 
	singlelinecheck=off
}

\DeclareCaptionLabelFormat{tablel}{Tabelul #2}
\captionsetup[table]{labelfont=bf, labelformat=tablel}

\captionsetup[figure]{
	labelsep=dash,
	font={normalfont},
	format=plain
}



% #####
% Abbreviations:
% #####

\newglossarystyle{myAcr} {
  \setglossarystyle{list}
  \renewcommand*{\glossentry}[2] {
  \item[\normalfont \bfseries \glsentryitem{##1} \glstarget{##1} {\glossentryname{##1}}] - \glossentrydesc{##1}}
}

% \makeglossaries % Doesn't work.
\makenoidxglossaries

\newacronym{glo:5g}{5G}{5th Generation}

\newacronym{glo:cli}{CLI}{Command Line Interface}



% #####
% Settings for bibliography:
% #####

\addbibresource{references.bib}

\setlength{\biblabelsep}{5pt}

\DeclareFieldFormat{labelnumberwidth}{#1\adddot}