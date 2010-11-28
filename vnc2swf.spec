%define	name	vnc2swf
%define	version	0.5.0
%define	release	%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Video
URL:		http://www.unixuser.org/~euske/vnc2swf/
Source:		http://www.unixuser.org/~euske/%{name}/%{name}-%{version}.tar.bz2
#		http://lists.kde.org/?l=kde-promo&m=104430062329339&q=raw
Source1:	vnc2swf-howto.txt
Patch0:		vnc2swf-0.5.0-fix-str-fmt.patch
Summary:	Tool for recording VNC sessions to Shockwave Flash
BuildRequires:	X11-devel xpm-devel
Requires:	vnc
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Vnc2swf is a recording tool for VNC, a protocol to manipulate 
remote window systems via network, developed by AT&T Laboratories 
Cambridge. It records VNC sessions and generates a Macromedia 
Flash movie file (SWF). It can be used as an X11 recorder or a 
Windows desktop recorder.

For instructions on using it, see vnc2swf-howto.txt in the documentation
directory.

%prep
%setup -q 
%patch0 -p0 -b .str

%build
%configure --prefix=%{_prefix}
%make 

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
find $RPM_BUILD_ROOT/%{_prefix} -type f -exec mv {} $RPM_BUILD_ROOT/%{_bindir} \;

cp %{SOURCE1} .

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%doc README* LICENCE.TXT vnc2swf-howto.txt


