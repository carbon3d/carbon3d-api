# Definitions
## Printer and Print Status Information
**Printer:** A Carbon built machine where final part(s) printed in the desired material.

**Prints:** A specific set of summary information related to a specific print generated from a Carbon Printer.

## Mass Custom and Production Part Endpoints (Requires Access to the Carbon Factory Platform)
**Models:** A file representing a three-dimensional geometry with no particular orientation, supports, etc. Models can belong to multiple parts.

**Parts:** A printable model design which includes DLS-specific data, such as a specific orientation, resin, etc.

**Part Orders:** A logical grouping of parts you would like to be auto packed on as few builds as possible.

**Print Orders:** A single build that you would like to queue X times on Y printers.

**Builds:** A printable set of parts arranged on a build platform ready for printing associated with a specific version of a project.

**Printer Queue:** An ordered list of builds in a given printer's queue.

**Printed Parts:** A specific instance of a part that has been printed and properly serialized.

**Part Measurements:** Measurements taken on a specific printed parts and logged in Carbon's cloud quality management system.

**Part Measurement Templates:** Templates for defining a part measurement to be taken and pass / failing criteria (e.g. length, width, visual inspection).