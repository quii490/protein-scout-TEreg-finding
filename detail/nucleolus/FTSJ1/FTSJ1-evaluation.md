---
type: protein-evaluation
gene: "FTSJ1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FTSJ1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FTSJ1 |
| 蛋白大小 | 329 aa |
| UniProt ID | Q9UET6 (tRNA (cytidine(32)/guanosine(34)-2'-O)-m) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FTSJ1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FTSJ1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | x4 | 28 | HPA 标注: Nucleoli |
| 📏 蛋白大小 | 10/10 | x1 | 10 | 329 aa |
| 🆕 研究新颖性 | 8/10 | x5 | 40 | PubMed 34 篇 |
| 🏗️ 三维结构 | 8/10 | x3 | 24 | AlphaFold pLDDT 84.8, v6 |
| 🧬 调控结构域 | 7/10 | x2 | 14 | InterPro 5 个结构域条目 |
| 🔗 PPI 网络 | 8/10 | x3 | 24 | STRING 30 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
| **原始总分** |  |  | **140.5/183** |  |
| **归一化总分** |  |  | **76.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | Nucleoli | Tier1 |
| UniProt | ,  | — |

**结论**: HPA 标注: Nucleoli。核定位得分 7/10。

**IF 图片**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 329 aa
- 大小适宜性评分：10/10

**评价**: 329 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 34 |
| 新颖性评分 | 8/10 |

**关键文献**:
1. Nease et al. (2024). "Selenocysteine tRNA methylation promotes oxidative stress resistance in melanoma metastasis.". *Nat Cancer*. PMID: 39438623
2. Brazane et al. (2023). "The ribose methylation enzyme FTSJ1 has a conserved role in neuron morphology and learning performance.". *Life Sci Alliance*. PMID: 36720500
3. Wang et al. (2025). "The role and machine learning analysis of mitochondrial autophagy-related gene expression in lung adenocarcinoma.". *Front Immunol*. PMID: 40313958
4. Wang et al. (2024). "Downregulation of tRNA methyltransferase FTSJ1 by PM2.5 promotes glycolysis and malignancy of NSCLC via facilitating PGK1 expression and translation.". *Cell Death Dis*. PMID: 39695074
5. Ishiguro et al. (2025). "Structural insights into tRNA recognition of the human FTSJ1-THADA complex.". *Commun Biol*. PMID: 40483304
**评价**: PubMed 34 篇，属于非常新颖，少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 84.8 |
| 有序区域 (pLDDT>70) 占比 | 84.8% |
| pLDDT>90 占比 | 62.6% |
| pLDDT 70-90 占比 | 22.2% |
| pLDDT 50-70 占比 | 5.2% |
| pLDDT<50 占比 | 10.0% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/FTSJ1/FTSJ1-PAE.png]]

**评价**: AlphaFold高质量预测（pLDDT=84.8）。有高置信度折叠域，结构可信度高。评分 8/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| Ribosomal RNA methyltransferase, FtsJ domain | IPR |
| Ribosomal RNA large subunit methyltransferase E | IPR |
| tRNA (cytidine(32)/guanosine(34)-2-O)-methyltransferase TRM7 | IPR |
| S-adenosyl-L-methionine-dependent methyltransferase superfamily | IPR |
| Ribosomal RNA large subunit methyltransferase RlmE | IPR |

**染色质调控潜力分析**: InterPro 注释了 5 个结构域条目。包含其他结构域类型。评分 7/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| TKT | anti bait coimmunoprecipitation | 17353931 | — | — |
| TMED10 | anti bait coimmunoprecipitation | 17353931 | — | — |
| PSMA3 | anti bait coimmunoprecipitation | 17353931 | — | — |
| TMEM33 | anti bait coimmunoprecipitation | 17353931 | — | — |
| TACO1 | anti bait coimmunoprecipitation | 17353931 | — | — |
| CBR1 | anti bait coimmunoprecipitation | 17353931 | — | — |
| 40982580 | anti bait coimmunoprecipitation | 17353931 | — | — |
| RPS9 | anti bait coimmunoprecipitation | 17353931 | — | — |
| CACYBP | anti bait coimmunoprecipitation | 17353931 | — | — |
| RPS3A | anti bait coimmunoprecipitation | 17353931 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| WDR6 | 0.995 | — | — |
| THADA | 0.977 | — | — |
| RSL24D1 | 0.921 | — | — |
| WDR74 | 0.910 | — | — |
| GTPBP4 | 0.907 | — | — |
| NSA2 | 0.889 | — | — |
| NIP7 | 0.886 | — | — |
| SLC38A5 | 0.876 | — | — |
| PES1 | 0.871 | — | — |
| BOP1 | 0.869 | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 30 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 30 个互作伙伴。评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 84.8 | — |
| 结构域 | InterPro | 5 个条目 | — |
| PPI | STRING | 30 partners | — |
| 定位 | HPA / UniProt | Nucleoli | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 较新颖，PubMed ≤100 篇
2. AlphaFold 结构质量好 (pLDDT>80)

**风险/不确定性**:
1. 结构可接受
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FTSJ1 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FTSJ1 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UET6
- Protein Atlas: https://www.proteinatlas.org/search/FTSJ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UET6
- STRING: https://string-db.org/network/9606.FTSJ1
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9UET6/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FTSJ1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/FTSJ1/FTSJ1-PAE.png]]


