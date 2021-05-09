using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace PartsTrackerApp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        public MainWindow()
        {
            InitializeComponent();
        }

        private void AddPartsButton_Click(object sender, RoutedEventArgs e)
        {
            AddPart addPart = new AddPart();
            addPart.Show();
            this.Close();
        }

        private void ManagePartsButton_Click(object sender, RoutedEventArgs e)
        {
            ManageParts manageParts = new ManageParts();
            manageParts.Show();
            this.Close();
        }

        private void ViewPartsButton_Click(object sender, RoutedEventArgs e)
        {
            ViewAllParts viewAllParts = new ViewAllParts();
            viewAllParts.Show();
            this.Close();
        }
    }
}
