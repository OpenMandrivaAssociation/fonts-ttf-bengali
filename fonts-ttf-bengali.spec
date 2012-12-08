Summary: A set of Bangla fonts under GPL
Name: fonts-ttf-bengali
# version number is defined at http://www.bengalinux.org/downloads/
Version: 0.5
Release: %mkrel 13
License: GPL
Group: System/Fonts/True type
Source0: http://savannah.nongnu.org/download/freebangfont/Akaash-0.8.5.tar.bz2
Source1: http://savannah.nongnu.org/download/freebangfont/Ani.tar.bz2
Source2: http://savannah.nongnu.org/download/freebangfont/Likhan-0.5.tar.bz2
Source3: http://savannah.nongnu.org/download/freebangfont/MuktiNarrow-0.94.tar.bz2
URL: http://www.bengalinux.org/
BuildArch:	noarch
BuildRequires: fontconfig
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





%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.5-11mdv2011.0
+ Revision: 675410
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.5-10
+ Revision: 675174
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5-9
+ Revision: 664323
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-8mdv2011.0
+ Revision: 605190
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.5-7mdv2010.1
+ Revision: 494131
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.5-6mdv2009.1
+ Revision: 351042
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.5-5mdv2009.0
+ Revision: 220859
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.5-4mdv2008.1
+ Revision: 125107
- kill re-definition of %%buildroot on Pixel's request


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:10:44 (52885)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 20:59:01 (52792)
- import fonts-ttf-bengali-0.5-3mdk

* Tue Feb 07 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5-3mdk
- Don't package fontconfig cache file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)

* Tue Aug 10 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.5-2mdk
- corrected License: tag

* Tue Aug 10 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.5-1mdk
- updated to Akaash 0.8.5, Ani 0.7.0, Likhan 0.5, MuktiNarrow 0.94

