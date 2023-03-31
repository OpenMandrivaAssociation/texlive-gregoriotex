Name:		texlive-gregoriotex
Version:	58331
Release:	2
Summary:	Engraving Gregorian Chant scores
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gregoriotex
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gregoriotex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gregoriotex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gregoriotex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Gregorio is a software application for engraving Gregorian
Chant scores on a computer. Gregorio's main job is to convert a
gabc file (simple text representation of a score) into a
GregorioTeX file, which makes TeX able to create a PDF of your
score.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/luatex/gregoriotex
%{_texmfdistdir}/texmf-dist/tex/luatex/gregoriotex
%{_texmfdistdir}/texmf-dist/tex/lualatex/gregoriotex
%{_texmfdistdir}/texmf-dist/scripts/gregoriotex
%{_texmfdistdir}/texmf-dist/fonts/truetype/public/gregoriotex
%doc %{_texmfdistdir}/texmf-dist/fonts/source/gregoriotex
%doc %{_texmfdistdir}/texmf-dist/doc/luatex/gregoriotex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
