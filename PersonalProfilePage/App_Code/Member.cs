namespace FreeconDB
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    public partial class Member
    {
        [Key]
        [StringLength(40)]
        public string UserName { get; set; }

        [StringLength(40)]
        public string FirstName { get; set; }

        [StringLength(40)]
        public string LastName { get; set; }

        public int? balance { get; set; }

        [StringLength(25)]
        public string email { get; set; }

        [StringLength(128)]
        public string password { get; set; }

        public long? phoneNumber { get; set; }

        [StringLength(128)]
        public string Address { get; set; }

        [StringLength(128)]
        public string Photo { get; set; }

        [StringLength(500)]
        public string summary { get; set; }
    }
}
