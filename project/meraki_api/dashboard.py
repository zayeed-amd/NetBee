# https://docs.google.com/presentation/d/1f0ja-N4gy6OZbIK91LoTz2FXgdmPlyhsgiw7TUTFq_8/edit#slide=id.g14b4003b687_0_195

import meraki

sandbox_api = "e3d51c21a25db0b843f33b7ef7bda6bc61192765"  # do not delete
zac_api = "bab27aa19220dfab302ab6a68c3bd21bc8b00f7a"
dashboard = meraki.DashboardAPI(api_key=sandbox_api, output_log=False, print_console=False)
