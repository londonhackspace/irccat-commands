package PubStandards::Dates;

use Modern::Perl;
use Moose;
use MooseX::FollowPBP;
use MooseX::Method::Signatures;

use Date::Manip;
use Time::DaysInMonth;

use constant MONTHS => qw( 
        0
        January  February  March      April    May       June 
        July     August    September  October  November  December
    );

method get_next_pubstandards_date {
    my $now   = time();
    my $month = (localtime $now)[4]+1;
    my $year  = (localtime $now)[5]+1900;
    
    $month++;
    if ( $month == 13 ) {
        $month = 1;
        $year++;
    }
    
    return $self->get_middle_thursday_of_month( $year, $month );
}
method get_year_of_pubstandards_dates {
    my $now   = time();
    my $month = (localtime $now)[4]+1;
    my $year  = (localtime $now)[5]+1900;
    my @dates;
    
    while ( scalar @dates <= 12 ) {
        $month++;
        if ( $month == 13 ) {
            $month = 1;
            $year++;
        }
        
        push @dates, $self->get_middle_thursday_of_month( $year, $month );
    }
    
    return @dates;
}

method get_middle_thursday_of_month ( Int $year!, Int $month! ) {
    my $month_name = (MONTHS)[$month];
    my $days       = days_in( $year, $month );
    my $middle_day = int $days / 2;
    
    my $middle = UnixDate(
            "${middle_day} ${month_name} ${year} at 23:59:59",
            '%s'
        );
    my $second = UnixDate(
            "2nd Thursday of ${month_name} ${year} at 18:00",
            '%s'
        );
    my $third  = UnixDate(
            "3rd Thursday of ${month_name} ${year} at 18:00",
            '%s'
        );
    
    my $second_delta = abs $second - $middle;
    my $third_delta  = abs $third  - $middle;
    
    return $third_delta < $second_delta
               ? $third
               : $second;
}

method get_name_for_month ( Int $month ) {
    return (MONTHS)[$month];
}

1;
