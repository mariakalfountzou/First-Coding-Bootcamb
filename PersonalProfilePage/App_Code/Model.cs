namespace FreeconDB
{
    using System;
    using System.Data.Entity;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Linq;

    public partial class FreeconDB : DbContext
    {
        public FreeconDB()
            : base("name=FreeconDB")
        {
        }

        public virtual DbSet<Member> Members { get; set; }
        public virtual DbSet<Service> Services { get; set; }

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Service>()
              .Property(e => e.Category)
              .IsUnicode(false);

            modelBuilder.Entity<Service>()
                .Property(e => e.ServiceName)
                .IsUnicode(false);
        }
    }
}
