%global tl_name gregoriotex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.1.0
Release:	%{tl_revision}.1
Summary:	Engraving Gregorian Chant scores
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/gregoriotex
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gregoriotex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gregoriotex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gregoriotex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(gregoriotex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Gregorio is a software application for engraving Gregorian Chant scores
on a computer. Gregorio's main job is to convert a gabc file (simple
text representation of a score) into a GregorioTeX file, which makes TeX
able to create a PDF of your score.

