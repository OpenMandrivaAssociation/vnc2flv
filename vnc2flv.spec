Name:		vnc2flv
Version:	20100207
Release:	3
License:	MIT
Group:		Video
URL:		https://www.unixuser.org/~euske/python/vnc2flv/index.html
Source:		http://pypi.python.org/packages/source/v/vnc2flv/%{name}-%{version}.tar.gz
Summary:	Screen recording tool that captures a VNC session and saves as FLV
BuildRequires:	python-devel
Requires:	x11vnc
Obsoletes:	vnc2swf
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Vnc2flv is a screen recorder. It captures a VNC desktop session and saves it as
a Flash Video (FLV) file.

%prep
%setup -q 

%build
python setup.py build

%install
rm -Rf $RPM_BUILD_ROOT
python setup.py install --root=%{buildroot}

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/index.html
%{_bindir}/*
%{py_platsitedir}/*


%changelog
* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 20100207-1mdv2011.0
+ Revision: 602222
- vnc2fv obsoleted vnc2swf
- renamed project

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.5.0-8mdv2010.0
+ Revision: 445698
- rebuild

* Sat Mar 28 2009 Funda Wang <fwang@mandriva.org> 0.5.0-7mdv2009.1
+ Revision: 362016
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-6mdv2009.0
+ Revision: 255580
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-4mdv2008.1
+ Revision: 171163
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix spacing at top of description

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5.0-3mdv2008.1
+ Revision: 136571
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Mar 18 2007 Buchan Milne <bgmilne@mandriva.org> 0.5.0-3mdv2007.1
+ Revision: 146176
- Rebuild
- Import vnc2swf

* Sun Jan 15 2006 Marcel Pol <mpol@mandriva.org> 0.5.0-2mdk
- remove claim from description about flash being a de facto standard

* Tue Dec 13 2005 Buchan Milne <bgmilne@mandriva.org> 0.5.0-1mdk
- New release 0.5.0
- drop patch0
- no longer buildrequires ming-devel

* Sun Jul 18 2004 Franck Villaume <fvill@freesurf.fr> 0.4.2-1mdk
- new version 0.4.2
- patch writeswf.c for ming 0.3

