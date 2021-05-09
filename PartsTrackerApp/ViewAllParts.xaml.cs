using System;
using System.Collections.Generic;
using System.Data.SqlClient;
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
using System.Windows.Shapes;
using System.Configuration;

namespace PartsTrackerApp
{
    /// <summary>
    /// Interaction logic for ViewAllParts.xaml
    /// </summary>
    public partial class ViewAllParts : Window
    {
        private Part part;

        public ViewAllParts()
        {
            InitializeComponent();
        }

        private void BackButton_Click(object sender, RoutedEventArgs e)
        {
            MainWindow main = new MainWindow();
            main.Show();
            this.Close();
        }

        private void Grid_Loaded(object sender, RoutedEventArgs e)
        {
            string connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";
            string sqlSelect = "SELECT * FROM Parts";
            SqlConnection conn = new SqlConnection(connString);

            SqlCommand cmd = new SqlCommand(sqlSelect, conn);

            try
            {
                conn.Open();
                SqlDataReader rdr = cmd.ExecuteReader();

                while(rdr.Read())
                {

                    part = new Part(rdr["Name"].ToString(), rdr["Part Number"].ToString(), rdr["Location"].ToString(), rdr["Unit Family"].ToString());

                    this.displayListBox.Items.Add(part);
                }
            }
            catch(SqlException ex)
            {
                MessageBox.Show(ex.Message + ex.StackTrace, "Exception Details");
            }
            finally
            {
                conn.Close();
            }
        }
    }
}
