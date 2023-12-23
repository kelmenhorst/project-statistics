import pandas as pd 

simple_features = ['domain', 'tri_category', 'avg_read_bytes', 'total_read_bytes', 'max_read_burst_len', 'avg_iat']
simple_domains = [
	"www.facebook.com",
    "twitter.com",
    "www.youtube.com",
    "www.instagram.com",
]

def get_packet_df(date):
	df = pd.read_csv("~/UACh/estadistica/proyecto/packets_final_with_domains_{}.csv".format(date))
	return df

def get_packet_df_simple(date, domain_subset = simple_domains):
	df_packets = get_packet_df(date)
	df = df_packets[df_packets["domain"].isin(domain_subset)]
	df = df.dropna()
	df = df.reset_index(drop=True)
	return df

def get_flow_df(date):
	df = pd.read_csv("~/UACh/estadistica/proyecto/flows_final_{}.csv".format(date))
	df = df[df['total_read_bytes'] > 0]
	df = df.dropna()
	df = df.reset_index(drop=True)
	return df

def get_flow_df_simple(date, features = simple_features, domain_subset = simple_domains):
	df_flows = get_flow_df(date)
	df = df_flows[features]
	df = df.dropna()
	df = df[df["domain"].isin(domain_subset)]
	df = df.reset_index(drop=True)
	return df



