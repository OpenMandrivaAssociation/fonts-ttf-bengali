Summary: A set of Bangla fonts under GPL
Name: fonts-ttf-bengali
# version number is defined at http://www.bengalinux.org/downloads/
Version: 0.5
Release: %mkrel 7
License: GPL
Group: System/Fonts/True type
Source0: http://savannah.nongnu.org/download/freebangfont/Akaash-0.8.5.tar.bz2
Source1: http://savannah.nongnu.org/download/freebangfont/Ani.tar.bz2
Source2: http://savannah.nongnu.org/download/freebangfont/Likhan-0.5.tar.bz2
Source3: http://savannah.nongnu.org/download/freebangfont/MuktiNarrow-0.94.tar.bz2
URL: http://www.bengalinux.org/
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools

Provides: fonts-tt-Akaash
Provides: fonts-tt-Ani
Provides: fonts-tt-Likhan
Provides: fonts-tt-MuktiNarrow

%description
This package contains a set of Bangla (Bengali) OpenType fonts based on
Unicode encoding scheme. The fonts are provided by Free Bangla Font project,
a sub project of Ankur group (http://www.bengalinux.org).

Install freebanglafont if you'd like to use Bangla or want to see Bangla
interface for GNOME, KDE, etc.

%prep
%setup -c -a 0 -a 1 -a 2 -a 3 -q

%build

%install
rm -rf %buildroot
install -d %buildroot/%_datadir/fonts/TTF/bengali

for i in `find . -name "*.ttf"` ; do
install -m 644 $i %buildroot/%_datadir/fonts/TTF/bengali
done
for i in `find . -name "*.TTF"` ; do
  install -m 644 $i \
	 %buildroot/%_datadir/fonts/TTF/bengali/`basename $i .TTF`.ttf
done

mkdir -p %buildroot/%_docdir/%{name}-%{version}/Akaash/
install -m 644 Akaash/{BUGS,README,MAILINGLISTS,VERSION,CHANGELOG,CREDITS} \
	%buildroot/%_docdir/%{name}-%{version}/Akaash/
mkdir -p %buildroot/%_docdir/%{name}-%{version}/Ani/
install -m 644 Ani/{AUTHORS,BUGS,MAILINGLISTS,README,VERSION} \
	%buildroot/%_docdir/%{name}-%{version}/Ani/
mkdir -p %buildroot/%_docdir/%{name}-%{version}/Likhan/
install -m 644 Likhan-0.5/README \
	%buildroot/%_docdir/%{name}-%{version}/Likhan/
mkdir -p %buildroot/%_docdir/%{name}-%{version}/MuktiNarrow/
install -m 644 MuktiNarrow0.94/readme.txt \
	%buildroot/%_docdir/%{name}-%{version}/MuktiNarrow/
install -m 644 Ani/COPYING %buildroot/%_docdir/%{name}-%{version}/

%post
touch %{_datadir}/fonts/TTF

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc %_docdir/%{name}-%{version}/*
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/bengali
%_datadir/fonts/TTF/bengali/*.ttf



