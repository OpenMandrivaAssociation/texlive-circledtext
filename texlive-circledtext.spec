%global tl_name circledtext
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Create circled text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/circledtext
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/circledtext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/circledtext.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides a macro \circledtext to typeset circled
text. Its starred version can produce an inverted version.

