---
type: protein-evaluation
gene: "FOXK2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
---

## FOXK2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXK2 |
| 蛋白大小 | 660 aa |
| UniProt ID | Q01167 (Forkhead box protein K2) |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXK2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXK2/IF_images/U-251MG_1.jpg|U-251MG]]


### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | x4 | 32 | HPA 标注: Nucleoplasm |
| 📏 蛋白大小 | 10/10 | x1 | 10 | 660 aa |
| 🆕 研究新颖性 | 4/10 | x5 | 30 | PubMed 74 篇 |
| 🏗️ 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT 56.4, v6 |
| 🧬 调控结构域 | 10/10 | x2 | 20 | InterPro 9 个结构域条目 |
| 🔗 PPI 网络 | 8/10 | x3 | 24 | STRING 30 partners |
| ➕ 互证加分 | — | max +3 | +0.5 | 核候选保守蛋白基线 |
|  | **原始总分** |  | **124.5/183** | **124.0/183** |  |  |  |
|  | **归一化总分** |  | **68.0/100** | **67.8/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | Nucleoplasm | Tier1 |
| UniProt | ,  | — |

**结论**: HPA 标注: Nucleoplasm。核定位得分 8/10。

**IF 图片**: 暂无数据（HPA IF 图像已本地嵌入。


#### 3.2 蛋白大小评估
- 660 aa
- 大小适宜性评分：10/10

**评价**: 660 aa 蛋白，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 74 |
| 新颖性评分 | 6/10 |

**评价**: PubMed 74 篇，属于有一定研究但 niche 空间充足。

**关键文献**:
1. Cai D et al. (2025). "Foxk1 and Foxk2 promote cardiomyocyte proliferation and heart regeneration". *Nat Commun*. PMID: 40128196
2. Zhang H et al. (2025). "A ROS-mediated oxidation-O-GlcNAcylation cascade governs ferroptosis". *Nat Cell Biol*. PMID: 40681752
3. Chen Q et al. (2024). "FoxK1 and FoxK2 cooperate with ORF45 to promote late lytic replication of Kaposi's sarcoma-associated herpesvirus". *J Virol*. PMID: 39494902
4. Wu P et al. (2025). "FOXK2 in skeletal muscle development: a new pathogenic gene for congenital myopathy with ptosis". *EMBO Mol Med*. PMID: 40410591
5. Yu Y et al. (2024). "FOXK2 amplification promotes breast cancer development and chemoresistance". *Cancer Lett*. PMID: 38901667
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 56.4 |
| 有序区域 (pLDDT>70) 占比 | 29.4% |
| pLDDT>90 占比 | 23.3% |
| pLDDT 70-90 占比 | 6.1% |
| pLDDT 50-70 占比 | 6.5% |
| pLDDT<50 占比 | 64.1% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 查询中 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXK2/FOXK2-PAE.png]]

**评价**: AlphaFold预测质量偏低（pLDDT=56.4）。大量无序区域。评分 6/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| Forkhead-associated (FHA) domain | IPR |
| Fork head domain | IPR |
| SMAD/FHA domain superfamily | IPR |
| Fork head domain conserved site1 | IPR |
| Fork head domain conserved site 2 | IPR |
| Winged helix-like DNA-binding domain superfamily | IPR |
| Winged helix DNA-binding domain superfamily | IPR |
| Forkhead box protein K2, forkhead domain | IPR |

**染色质调控潜力分析**: InterPro 注释了 9 个结构域条目。包含 forkhead/winged-helix DNA 结合域，为典型转录因子。评分 10/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ASXL2 | 0.968 | — | — |
| SIN3A | 0.947 | — | — |
| ASXL1 | 0.942 | — | — |
| BAP1 | 0.941 | — | — |
| HCFC1 | 0.930 | — | — |
| KDM1B | 0.832 | — | — |
| OGT | 0.782 | — | — |
| RBBP7 | 0.731 | — | — |
| YY1 | 0.707 | — | — |
| NCOR2 | 0.704 | — | — |

**GO-CC 复合体**: 从 UniProt GO 注释提取

**PPI 互证分析**:
- STRING 高置信度 (>0.7) partners: 10 个
- 调控相关比例: 待进一步分析

**评价**: STRING 数据库显示 30 个互作伙伴。评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT 56.4 | — |
| 结构域 | InterPro | 9 个条目 | — |
| PPI | STRING | 30 partners | — |
| 定位 | HPA / UniProt | Nucleoplasm | — |

**互证加分明细**:
- 进化保守性: 核候选保守蛋白 → +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (4.0/5)

**核心优势**:
1. 较新颖，PubMed ≤100 篇
2. 核蛋白候选

**风险/不确定性**:
1. AlphaFold 预测质量偏低，大量无序区域
2. '研究数据有限，需更多实验验证'

**下一步建议**:
- [ ] 在 TEreg 系统中检测 FOXK2 表达及定位
- [ ] 通过 co-IP/MS 验证 PPI 网络
- [ ] ChIP-seq 检查 FOXK2 在 TE 区域的 occupancy

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01167
- Protein Atlas: https://www.proteinatlas.org/search/FOXK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01167
- STRING: https://string-db.org/network/9606.FOXK2
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q01167/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[FOXK2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXK2/FOXK2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q01167 |
| SMART | SM00339;SM00240; |
| UniProt Domain [FT] | DOMAIN 54..128; /note="FHA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00086" |
| InterPro | IPR047397;IPR000253;IPR047398;IPR001766;IPR008984;IPR018122;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00498;PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141568-FOXK2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IRF2 | Intact, Biogrid | true |
| TULP3 | Intact, Biogrid | true |
| ARID4A | Biogrid | false |
| ASXL1 | Biogrid | false |
| ASXL2 | Biogrid | false |
| BAP1 | Biogrid | false |
| BRD4 | Biogrid | false |
| CIC | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
