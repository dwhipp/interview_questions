#!/usr/bin/env perl6

constant @kNeighbors_n8 = ([X] (-1..1) xx 2).grep: { .all != 0 };

sub CountShapes(@image) {
  my @visited;

  my sub visit_point([$x, $y]) {
    return $y == any(@image.keys) && $x == any(@image[$y].keys) &&
           @image[$y][$x] eq 'X' && ! @visited[$y][$x]++
  }

  my sub visit_shape($initial_point) {
    return unless visit_point $initial_point;
    my @q = $initial_point;
    while @q {
      @q.push: |(@kNeighbors_n8 »+» (@q.shift, *)).grep: { visit_point $_ }
    }
    return True
  }

  return [+] @image.kv.map: -> $y, @row {
    elems @row.keys.grep: { visit_shape [$^x, $y] }
  }
}

say CountShapes $*IN.lines».comb».flat
