#!/usr/bin/env perl
#computeuse.pl
#20180206 (schober2) Entirely refactored and modularized
#20170725 (schober2) Fixed pinging behavior, formatting, general robustness
#20161227 (schober2) Reformatted code - 80 char friendly, combined scripts
#                    for multiple OSes, fixed some error handling, added
#                    comments, reformatted output slightly
#20170324 (schober2) Changed swap display and added uptime
#20170406 (schober2) Changed to strict and fixed 0 day uptime display
#20170530 (schober2) More nicely formatted output

use Net::Ping;
use lib '/egr/common/compute/lib/';
use COMPUSE;
use threads;
use strict;

my @hosts = qw(
  compute01
  compute02
  compute03
  compute04
  compute05
  compute06
  compute07
  compute08
  compute09
);

my $nccmd='nc --wait 1000ms --recv-only';
chomp(my $syshost = `hostname`);
if (grep $_ eq $syshost, ("scully","chavez")){
  $nccmd='nc -w 1 -d';
}

#Start pings to check if up.
my $p = Net::Ping->new("syn",1);
$p->port_number('22','tcp');
foreach my $host(@hosts){
  $p->ping($host,1);
}

#Run threaded to keep responsive
my @threads;
foreach (@hosts) {
  if ( $p->ack($_) ){
    push @threads, threads->new(\&COMPUSE::processHost, ($_, $nccmd, 0));
  } else {
    push @threads, threads->new(\&COMPUSE::unavailable, $_, 0);
  }
}
$p->close();

&COMPUSE::print_header;
#Print Output from each thread
foreach (@threads) {
  my $return = $_->join();
  if ($return ne '1'){
    print $return;
  }
}
&COMPUSE::print_footer
