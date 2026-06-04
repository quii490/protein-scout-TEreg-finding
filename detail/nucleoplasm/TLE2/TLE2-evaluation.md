---
type: protein-evaluation
gene: "TLE2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TLE2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TLE2 / ESG2|GRG2|ESG|FLJ41188 |
| 蛋白全称 | Transducin-like enhancer protein 2 |
| 蛋白大小 | 743 aa |
| UniProt ID | Q04725 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 743 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 43 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 12 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **111/183** | **110.0/183** |  |  |  |
|  | **归一化总分** |  | **60.7/100** | **60.1/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IDA|IEA|NAS |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TLE2/IF_images/MCF-7_HPA049103_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TLE2/IF_images/RT-4_HPA049103_2.jpg|RT-4]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 743 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 43 |

**评价**: PubMed 43 篇，高度新颖

**关键文献**:
1. Orozco LD et al. (2023). "A systems biology approach uncovers novel disease mechanisms in age-related macular degeneration". *Cell Genom*. PMID: 37388919
2. Wang Y et al. (2025). "RNA binding protein DDX3X drives pancreatic cancer progression via the TLE2-MYL9 axis". *Sci Adv*. PMID: 40938994
3. Hoffman BG et al. (2008). "Expression of Groucho/TLE proteins during pancreas development". *BMC Dev Biol*. PMID: 18778483
4. Hu S et al. (2020). "TLE2 is associated with favorable prognosis and regulates cell growth and gemcitabine sensitivity in pancreatic cancer". *Ann Transl Med*. PMID: 32953817
5. He Z et al. (2010). "Cellular corepressor TLE2 inhibits replication-and-transcription- activator-mediated transactivation and lytic reactivation of Kaposi's sarcoma-associated herpesvirus". *J Virol*. PMID: 19939918
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 743 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 12 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TLE2/TLE2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Groucho/TLE_N |
| InterPro | Groucho_enhance |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_repeat_CS |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| Pfam | TLE_N |
| Pfam | WD40 |
| SMART | WD40 |
| PROSITE | WD_REPEATS_1 |
| PROSITE | WD_REPEATS_2 |
| PROSITE | WD_REPEATS_REGION |

**染色质调控潜力分析**: 12 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:transcription regulator complex (GO:0005667, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 12 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 43 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TLE2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065717-TLE2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TLE2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q04725
- STRING: https://string-db.org/network/9606.ENSG00000065717
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q04725


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TLE2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TLE2/TLE2-PAE.png]]




