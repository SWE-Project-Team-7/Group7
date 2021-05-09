using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PartsTrackerApp
{
    public class Part
    {
        private string name;
        private string partNumber;
        private string location;
        private string unitFamily;

        
        public Part(string name, string partNumber, string location, string unitFamily)
        {
            this.name = name;
            this.partNumber = partNumber;
            this.location = location;
            this.unitFamily = unitFamily;
        }
        

        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                name = value;
            }
        }

        public string PartNumber
        {
            get
            {
                return partNumber;
            }
            set
            {
                partNumber = value;
            }
        }

        public string Location
        {
            get
            {
                return location;
            }
            set
            {
                location = value;
            }
        }

        public string UnitFamily
        {
            get
            {
                return unitFamily;
            }
            set
            {
                location = value;
            }
        }

        public override string ToString()
        {
            return String.Format("{0, -10} {1, 20} {2, 20} {3, 20}", name, partNumber ,location, unitFamily);
        }
    }
}
