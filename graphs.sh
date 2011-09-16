#!/bin/bash
shift; shift; shift; shift

case "$1" in
  'power')
  echo 'http://hack.rs/cacti/graph_view.php?action=tree&tree_id=2'
;;
  'laser')
  echo 'http://hack.rs/cacti/graph_view.php?action=tree&tree_id=7'
;;
  *)
  echo "Hackspace monitoring graphs: http://hack.rs/cacti"
;;
esac
