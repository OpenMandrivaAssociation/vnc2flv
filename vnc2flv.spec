Name:		vnc2flv
Version:	20100207
Release:	%mkrel 1
License:	MIT
Group:		Video
URL:		http://www.unixuser.org/~euske/python/vnc2flv/index.html
Source:		http://pypi.python.org/packages/source/v/vnc2flv/%{name}-%{version}.tar.gz
Summary:	Screen recording tool that captures a VNC session and saves as FLV
BuildRequires:	python-devel
Requires:	x11vnc
Obsoletes:	vnc2swf
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Vnc2flv is a screen recorder. It captures a VNC desktop session and saves it as a Flash Video (FLV) file.

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
