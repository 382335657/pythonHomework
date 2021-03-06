
#include<stdio.h>

#include<vector>

#include<string.h>

using namespace std;

#define LL long long

#define mod 998244353

typedef struct

{

	int x, val;

}Res;

Res now;

vector<Res> G[100005];

int cnt, sum, ok, vis[100005], scc[100005];

LL all[100005], er[100005] = {1};

LL Pow(LL x, LL y)

{

	LL ans = 1;

	while(y)

	{

		if(y%2)

			ans = ans*x%mod;

		x = x*x%mod;

		y /= 2;

	}

	return ans;

}

void Sech(int u)

{

	int i, v, val;

	sum++;

	for(i=0;i<G[u].size();i++)

	{

		if(G[u][i].val==-1)

			continue;

		v = G[u][i].x;

		val = vis[u]^G[u][i].val;

		if(vis[v]==-1)

		{

			vis[v] = val;

			Sech(v);

		}

		else if(vis[v]!=val)

			ok = 1;

	}

}

void Sech2(int u, int k)

{

	int i, v;

	sum++;

	scc[u] = k;

	for(i=0;i<G[u].size();i++)

	{

		v = G[u][i].x;

		if(scc[v]==0)

			Sech2(v, k);

	}

}

int main(void)

{

	LL ans;

	int x, y, val, n, m, i;

	scanf("%d%d", &n, &m);

	for(i=1;i<=m;i++)

	{

		scanf("%d%d%d", &x, &y, &val);

		now.x = y, now.val = val;

		G[x].push_back(now);

		now.x = x;

		G[y].push_back(now);

	}

	for(i=1;i<=n;i++)

		er[i] = er[i-1]*2%mod;

	memset(vis, -1, sizeof(vis));

	for(i=1;i<=n;i++)

	{

		if(vis[i]==-1)

		{

			vis[i] = 0;

			Sech(i);

		}

	}

	if(ok)

		printf("0\n");

	else

	{

		ans = 1;

		for(i=1;i<=n;i++)

		{

			if(scc[i]==0)

			{

				sum = 0;

				Sech2(i, ++cnt);

				all[cnt] = er[sum-1];

			}

		}

		memset(vis, -1, sizeof(vis));

		for(i=1;i<=n;i++)

		{

			if(vis[i]==-1)

			{

				sum = 0;

				vis[i] = 0;

				Sech(i);

				all[scc[i]] = all[scc[i]]*Pow(er[sum-1], mod-2)%mod;

			}

		}

		for(i=1;i<=cnt;i++)

			ans = ans*all[i]%mod;

		printf("%lld\n", ans);

	}

	return 0;

}

/*

3 3

1 2 1

2 3 1

3 1 1

*/
