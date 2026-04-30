\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{utmreport}[2026/04/30 Universal UTM report and thesis class]

\LoadClass[12pt,a4paper]{report}

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
\RequirePackage[romanian,english]{babel}
\RequirePackage{graphicx}
\RequirePackage{amsmath}
\RequirePackage{array}
\RequirePackage{tabularx}
\RequirePackage{longtable}
\RequirePackage{caption}
\RequirePackage{enumitem}
\RequirePackage{indentfirst}
\RequirePackage{setspace}
\RequirePackage{titlesec}
\RequirePackage{tocloft}
\RequirePackage{ragged2e}
\RequirePackage{listings}
\RequirePackage{xcolor}

\selectlanguage{romanian}
\setstretch{1.5}
\setlength{\parindent}{1.25cm}
\setlength{\parskip}{0pt}
\pagestyle{plain}

\titleformat{\chapter}[block]
  {\centering\bfseries\fontsize{14pt}{16pt}\selectfont}
  {\thechapter}
  {1em}
  {}
\titlespacing*{\chapter}{0pt}{0pt}{12pt}

\titleformat{\section}
  {\bfseries\fontsize{12pt}{14pt}\selectfont}
  {\thesection}
  {1em}
  {}
\titlespacing*{\section}{0pt}{12pt}{0pt}

\titleformat{\subsection}
  {\bfseries\fontsize{12pt}{14pt}\selectfont}
  {\thesubsection}
  {1em}
  {}
\titlespacing*{\subsection}{0pt}{12pt}{0pt}

\setcounter{tocdepth}{2}
\renewcommand{\cftchapleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cfttoctitlefont}{\hfill\bfseries\fontsize{14pt}{16pt}\selectfont}
\renewcommand{\cftaftertoctitle}{\hfill}
\setlength{\cftbeforechapskip}{0pt}

\setlist[itemize]{leftmargin=1.25cm,itemsep=0pt,topsep=0pt,parsep=0pt,partopsep=0pt}
\setlist[enumerate]{leftmargin=1.25cm,itemsep=0pt,topsep=0pt,parsep=0pt,partopsep=0pt}
\newenvironment{utmenumerate}{\begin{enumerate}[label=\alph*)]}{\end{enumerate}}

\numberwithin{equation}{chapter}
\numberwithin{figure}{chapter}
\numberwithin{table}{chapter}
\renewcommand{\figurename}{Figura}
\renewcommand{\tablename}{Tabelul}
\DeclareCaptionLabelSeparator{dash}{ - }
\captionsetup[figure]{labelsep=dash,justification=centering,singlelinecheck=true,font=normalfont}
\captionsetup[table]{labelsep=dash,justification=raggedleft,singlelinecheck=false,labelfont=bf}

\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}
\renewcommand{\arraystretch}{1.2}

\lstdefinestyle{utmcode}{
  basicstyle=\ttfamily\fontsize{10pt}{12pt}\selectfont,
  breaklines=true,
  frame=single,
  numbers=left,
  numberstyle=\tiny,
  tabsize=2,
  backgroundcolor=\color{gray!8}
}
\lstset{style=utmcode}

\newcommand{\UTMLogoPath}{../shared/UTM_Logo.png}
\newcommand{\utmlogo}[1]{\renewcommand{\UTMLogoPath}{#1}}

\newcommand{\institution}[1]{\gdef\UTMInstitution{#1}}
\newcommand{\faculty}[1]{\gdef\UTMFaculty{#1}}
\newcommand{\department}[1]{\gdef\UTMDepartment{#1}}
\newcommand{\reporttitle}[1]{\gdef\UTMReportTitle{#1}}
\newcommand{\reportsubtitle}[1]{\gdef\UTMReportSubtitle{#1}}
\newcommand{\student}[2]{\gdef\UTMStudentName{#1}\gdef\UTMStudentGroup{#2}}
\newcommand{\supervisor}[2]{\gdef\UTMSupervisorName{#1}\gdef\UTMSupervisorTitle{#2}}
\newcommand{\consultant}[2]{\gdef\UTMConsultantName{#1}\gdef\UTMConsultantTitle{#2}}
\newcommand{\cityyear}[2]{\gdef\UTMCity{#1}\gdef\UTMYear{#2}}
\newcommand{\documenttype}[1]{\gdef\UTMDocumentType{#1}}

\institution{Universitatea Tehnică a Moldovei}
\faculty{Facultatea}
\department{Departamentul}
\reporttitle{Titlul lucrării}
\reportsubtitle{}
\student{Prenumele NUMELE}{grupa}
\supervisor{Prenumele NUMELE}{titlul științific}
\consultant{}{}
\cityyear{Chișinău}{2026}
\documenttype{Raport}

\newcommand{\makeutmcover}{%
  \begin{titlepage}
  \centering
  \includegraphics[height=2cm]{\UTMLogoPath}\par\vspace{0.5cm}
  {\bfseries\fontsize{16pt}{18pt}\selectfont \UTMInstitution\par}
  \vspace{4cm}
  {\bfseries\fontsize{22pt}{26pt}\selectfont \UTMReportTitle\par}
  \ifx\UTMReportSubtitle\empty\else
    \vspace{0.5cm}{\bfseries\fontsize{16pt}{18pt}\selectfont \UTMReportSubtitle\par}
  \fi
  \vspace{3cm}
  \hfill\begin{minipage}{0.65\textwidth}
  \raggedright\bfseries\fontsize{16pt}{18pt}\selectfont
  Student: \UTMStudentName\\
  Grupa: \UTMStudentGroup\\[0.5cm]
  Conducător: \UTMSupervisorTitle, \UTMSupervisorName
  \end{minipage}
  \vfill
  {\bfseries\fontsize{16pt}{18pt}\selectfont \UTMCity{} - \UTMYear\par}
  \end{titlepage}
}

\newcommand{\makeutmreporttitlepage}{%
  \begin{titlepage}
  \centering
  {\bfseries\fontsize{12pt}{14pt}\selectfont
  Ministerul Educației și Cercetării al Republicii Moldova\\
  \UTMInstitution\\
  \UTMFaculty\\
  \UTMDepartment\par}
  \vspace{2.2cm}
  \includegraphics[height=2cm]{\UTMLogoPath}\par
  \vspace{2cm}
  {\bfseries\fontsize{20pt}{24pt}\selectfont \UTMReportTitle\par}
  \ifx\UTMReportSubtitle\empty\else
    \vspace{0.6cm}{\bfseries\fontsize{14pt}{17pt}\selectfont \UTMReportSubtitle\par}
  \fi
  \vspace{0.8cm}
  {\bfseries\fontsize{16pt}{19pt}\selectfont \UTMDocumentType\par}
  \vspace{2.2cm}
  \hfill\begin{minipage}{0.62\textwidth}
  \raggedright\bfseries\fontsize{12pt}{14pt}\selectfont
  Student: \UTMStudentName\\
  Grupa: \UTMStudentGroup\\[4pt]
  Conducător: \UTMSupervisorTitle, \UTMSupervisorName
  \end{minipage}
  \vfill
  {\bfseries\fontsize{12pt}{14pt}\selectfont \UTMCity{} - \UTMYear\par}
  \end{titlepage}
}

\newcommand{\makeutmthesistitlepage}{%
  \begin{titlepage}
  \centering
  {\bfseries\fontsize{12pt}{14pt}\selectfont
  Ministerul Educației și Cercetării al Republicii Moldova\\
  \UTMInstitution\\
  \UTMFaculty\\
  \UTMDepartment\par}
  \vspace{1.5cm}
  \hfill\begin{minipage}{0.45\textwidth}
  \raggedright\bfseries\fontsize{11pt}{13pt}\selectfont
  Admis la susținere\\
  Șef departament: \rule{4.5cm}{0.4pt}\\
  ``\rule{0.8cm}{0.4pt}''\rule{2.5cm}{0.4pt} \UTMYear
  \end{minipage}
  \vspace{2cm}
  {\bfseries\fontsize{20pt}{24pt}\selectfont \UTMReportTitle\par}
  \vspace{0.7cm}
  {\bfseries\fontsize{16pt}{19pt}\selectfont \UTMDocumentType\par}
  \vspace{2cm}
  \hfill\begin{minipage}{0.72\textwidth}
  \raggedright\bfseries\fontsize{12pt}{14pt}\selectfont
  Student: \rule{2.4cm}{0.4pt} \UTMStudentName, \UTMStudentGroup\\[4pt]
  Conducător: \rule{2.4cm}{0.4pt} \UTMSupervisorTitle, \UTMSupervisorName\\[4pt]
  \ifx\UTMConsultantName\empty\else Consultant: \rule{2.4cm}{0.4pt} \UTMConsultantTitle, \UTMConsultantName\\[4pt]\fi
  \end{minipage}
  \vfill
  {\bfseries\fontsize{12pt}{14pt}\selectfont \UTMCity{} - \UTMYear\par}
  \end{titlepage}
}

\newenvironment{utmabstract}[1][Rezumat]
  {\chapter*{#1}\addcontentsline{toc}{chapter}{#1}}
  {\clearpage}

\newcommand{\utmkeywords}[1]{\noindent\textbf{Cuvinte cheie:} #1\par}
