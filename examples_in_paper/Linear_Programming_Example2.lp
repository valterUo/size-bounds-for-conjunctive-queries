\ Model Linear_Programming_Example
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  xyz
Subject To
 Rel_xy: xy <= 1
 Rel_yz: yz <= 1
 Rel_zx: xz <= 1
 Monotonicity: - yz + xyz >= 0
 Monotonicity: - xz + xyz >= 0
 Monotonicity: - xy + xyz >= 0
 Submodularity: - z + xz + yz - xyz >= 0
 Submodularity: - y + xy + yz - xyz >= 0
 Submodularity: - x + xy + xz - xyz >= 0
 Subadditivity: x + y - xy >= 0
 Subadditivity: x + z - xz >= 0
 Subadditivity: y + z - yz >= 0
Bounds
 x <= 1
 y <= 1
 z <= 1
 xy <= 2
 xz <= 2
 yz <= 2
 xyz <= 3
End
