# Databricks notebook source
def dataLakeServicePrincipalConnectionInitiation(data_lake_service_principal_client_id_secret_reference, data_lake_service_principal_client_secret_secret_reference, tenant_id_secret_reference,secretScopeName = None):
    if(secretScopeName == None):
        secretScopeName = 'aaa-adb-scope'
    if(tenant_id_secret_reference == None):
        tenant_id = '1aa51068-11a6-4bd2-8646-1fff31a30ffc'
    else:
        tenant_id = dbutils.secrets.get(scope = secretScopeName, key = tenant_id_secret_reference)
    spark.conf.set("fs.azure.account.auth.type", "OAuth")
    spark.conf.set("fs.azure.account.oauth.provider.type", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
    spark.conf.set("fs.azure.account.oauth2.client.id", dbutils.secrets.get(scope = secretScopeName, key = data_lake_service_principal_client_id_secret_reference))
    spark.conf.set("fs.azure.account.oauth2.client.secret", dbutils.secrets.get(scope = secretScopeName, key = data_lake_service_principal_client_secret_secret_reference))
    spark.conf.set("fs.azure.account.oauth2.client.endpoint", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

    return True

# COMMAND ----------

def get_environment():
    """
    Get environment from the custom tags in the databricks workspace
    """
    usageTags = spark.conf.get("spark.databricks.clusterUsageTags.clusterAllTags")
    res = list(eval(usageTags))
    try:
        env_tag_value = [x for x in res if x["key"] == "Env"][0]["value"]
    except:
        env_tag_value = 'DEV'
        
    return env_tag_value
