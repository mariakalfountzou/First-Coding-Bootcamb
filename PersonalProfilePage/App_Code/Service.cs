namespace FreeconDB
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("Service")]
    public partial class Service
    {
        public int ServiceID { get; set; }

        [StringLength(40)]
        public string ServiceName { get; set; }

        [StringLength(40)]
        public string Category { get; set; }
    }
}
