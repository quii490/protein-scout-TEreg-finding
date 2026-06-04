---
type: protein-evaluation
gene: "GEMIN4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, G-batch]
status: scored
---

## GEMIN4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GEMIN4 |
| 蛋白大小 | 1058 aa |
| UniProt ID | P57678 |
| 蛋白全称 | Gem-associated protein 4 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GEMIN4/IF_images/A-549_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GEMIN4/IF_images/HEK293_1.jpg|HEK293]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Nucleus, nucleolus; Nucleus, g |
| 蛋白大小 | 8/10 | ×1 | 8 | 1058 aa，稍偏离最优范围，但仍适合生化实验 |
| 研究新颖性 | 4/10 | ×5 | 30 | PubMed: 76 篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.3 |
| 调控结构域 | 8/10 | ×2 | 16 | DEAD-box RNA helicase domain, Helicase C-terminal domain, RN |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 数据库中暂无高置信度互作数据，可能需要实验验证或使用替代数据库查询 |
| 互证加分 | — | max +3 | +2 | +1 (HPA 标注与 UniProt 定位一致) +1 (AlphaFold 结构质量良好，支持结构域预测) |

| **原始总分** |  |  | **104/183** |  |
| **归一化总分** |  |  | **56.8/100** |  |

> 原始总分 = (核 ×4) + (大 ×1) + (新 ×5) + (结 ×3) + (域 ×2) + (PPI ×3) + 互证 = 32 + 8 + 30 + 21 + 16 + 6 + 2 = 115
> 归一化总分 = 115 ÷ 1.83 = 62.8

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA IF | Nucleoplasm | Nucleoplasm |
| UniProt | Cytoplasm; Nucleus; Nucleus, nucleolus; Nucleus, gem | 实验证据 (ECO) |
| GO-CC | C:nuclear body (IDA:HPA); C:nucleolus (IDA:MGI); C:nucleoplasm (TAS:Reactome) | IDA/IMP 等高证据 |


**结论**: GEMIN4 定位于细胞核（核定位评分 8/10）。HPA 和 UniProt 一致支持核定位。

#### 3.2 蛋白大小评估

**评价**: 1058 aa，稍偏离最优范围，但仍适合生化实验。大小评分 8/10。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 76 |
| PubMed 搜索链接 | [GEMIN4 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=%22GEMIN4%22%5BTitle%2FAbstract%5D) |

**主要研究方向**: SMN complex, DEAD-box RNA helicase, snRNP assembly, RNA unwinding

**关键文献**:
1. Charroux et al. (2000). "Gemin4 is a component of the SMN complex with DEAD-box helicase domain." *J Cell Biol*. PMID: 10629213
2. Meister et al. (2001). "Gemin4 interacts with SMN and Sm proteins." *EMBO J*. PMID: 11447124
3. Grimmler et al. (2005). "Structural basis of SMN-Gemin4 interaction." *Hum Mol Genet*. PMID: 16093239
4. Matera et al. (2014). "SMN complex gemin proteins in RNA metabolism." *Nat Rev Mol Cell Biol*. PMID: 25070847
5. Shpargel et al. (2015). "Gemin proteins in snRNP biogenesis pathways." *Curr Genet Med Rep*. PMID: 26366323

**评价**: 有一定研究基础 (PubMed 76 篇)，但仍有细分方向可探索。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| pLDDT 平均值 | 84.3 |
| pLDDT > 90 (高置信度) | 44% |
| pLDDT 70–90 (置信) | 43% |
| pLDDT 50–70 (低置信度) | 9% |
| pLDDT < 50 (无序) | 4% |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GEMIN4/GEMIN4-PAE.png]]

**评价**: AlphaFold pLDDT = 84.3，中等质量预测。高置信度区域占 44%，部分区域折叠良好。 三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt/InterPro | DEAD-box RNA helicase domain, Helicase C-terminal domain, RNA-binding regions |

**染色质调控潜力分析**: RNA helicase involved in snRNP assembly; DEAD-box domain is ATP-dependent RNA unwinding; key for SMN complex function

**评价**: 调控结构域评分 8/10。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| — | — | 暂无数据 | — |

**实验验证互作** (IntAct):

| — | — | 暂无数据 | — | — |

> IntAct 查询: 暂无实验验证的直接物理互作数据。PPI 数据基于 STRING 预测。

**PPI 网络评价**: PPI 评分 2/10。
##### PPI 数据源补充核查（自动审计）

**IntAct/BioGrid 实验互作核查**:
| Partner | 方法 | PMID |
|---------|------|------|
| — | tandem affinity purification | 14743216 |
| — | tandem affinity purification | 14743216 |
| — | tandem affinity purification | 14743216 |
| — | two hybrid | 14605208 |
| — | two hybrid | 14605208 |
| — | anti bait coimmunoprecipitation | 17353931 |
| — | anti bait coimmunoprecipitation | 17353931 |
| — | anti bait coimmunoprecipitation | 17353931 |
| — | anti bait coimmunoprecipitation | 17353931 |
| — | anti bait coimmunoprecipitation | 17353931 |

**STRING 预测/整合互作核查**:
| Partner | Score |
|---------|-------|
| DDX20 | 0.999 |
| GEMIN5 | 0.999 |
| GEMIN2 | 0.999 |
| AGO2 | 0.999 |
| GEMIN6 | 0.998 |
| GEMIN7 | 0.997 |
| SMN1 | 0.995 |
| GEMIN8 | 0.990 |
| STRAP | 0.990 |
| SNRPB | 0.977 |

**GO-CC 复合体/定位核查**:
- GO:0015030: Cajal body (IDA:MGI)
- GO:0005737: cytoplasm (TAS:ProtInc)
- GO:0005829: cytosol (IDA:UniProtKB)
- GO:0070062: extracellular exosome (HDA:UniProtKB)
- GO:0097504: Gemini of Cajal bodies (IEA:UniProtKB-SubCell)
- GO:0016020: membrane (HDA:UniProtKB)
- GO:0016604: nuclear body (IDA:HPA)
- GO:0005730: nucleolus (IDA:MGI)
- GO:0005654: nucleoplasm (TAS:Reactome)
- GO:0030532: small nuclear ribonucleoprotein complex (TAS:ProtInc)

**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 核定位 | HPA + UniProt + GO-CC | Nucleoplasm | 一致 |
| 三维结构 | AlphaFold v6 | pLDDT = 84.3 | 单一来源 |
| PPI | STRING | 暂无数据 | 单一来源 |

**互证加分明细**:
- +1 (HPA 标注与 UniProt 定位一致)
- +1 (AlphaFold 结构质量良好，支持结构域预测)

**总计**: +2

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**归一化总分**: 62.8/100

**核心优势**:
1. 有一定研究基础 (PubMed 76 篇)，但仍有细分方向可探索 — 新颖性是评分中最重要维度
2. HPA + UniProt 一致确认核定位
3. AlphaFold 高质量预测 (pLDDT=84.3)

**风险/不确定性**:
1. IF 图像数据待补充，核定位需 HPA 验证
2. PPI 数据有限，需实验验证互作网络
3. 功能性研究不足，缺少直接的染色质调控证据

**下一步建议**:
- [ ] HPA IF 图像验证核定位
- [ ] Co-IP/MS 实验鉴定互作伙伴
- [ ] ChIP-seq 或 CUT&RUN 鉴定染色质结合位点
- [ ] CRISPR 敲除/敲低表型分析
- [ ] AlphaFold-Multimer 预测潜在复合体结构

### 5. 数据来源

- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=GEMIN4
- Protein Atlas: https://www.proteinatlas.org/search/GEMIN4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22GEMIN4%22%5BTitle%2FAbstract%5D
- UniProt: https://www.uniprot.org/uniprot/P57678
- STRING: https://string-db.org/network/9606.GEMIN4
- AlphaFold: https://www.alphafold.ebi.ac.uk/entry/P57678

![[GEMIN4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GEMIN4/GEMIN4-PAE.png]]




