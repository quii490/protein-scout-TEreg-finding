---
type: protein-evaluation
gene: "PROSER1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PROSER1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PROSER1 |
| 蛋白大小 | 944 aa |
| UniProt ID | Q86XN7 |
| 蛋白全称 | Proline and serine-rich protein 1 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PROSER1/IF_images/55687_if_selected_medium.jpg|55687_if_selected_medium]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | Nucleoplasm (Approved); UniProt: No specific annotation in UniProt; HPA Approved |
| 蛋白大小 | 8/10 | ×1 | 8 | 944 aa，稍偏小/偏大但仍在可行范围内 (100–200 或 800–1200 aa) |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed: 4 篇 |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=44.5; PDB: None |
| 调控结构域 | 8/10 | ×2 | 16 | Domain of unknown function DUF4476 |
| PPI 网络 | 4/10 | ×3 | 12 | STRING only textmining/co-expression predictions, no experimental evidence; TCF2... |
| 互证加分 | — | max +3 | +1 | +1 (HPA Approved + GO-CC IDA nucleoplasm confirmed) |

| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

> 原始总分 = (核 ×4) + (大 ×1) + (新 ×5) + (结 ×3) + (域 ×2) + (PPI ×3) + 互证 = 32 + 8 + 50 + 18 + 16 + 12 + 1 = 137
> 归一化总分 = 137 ÷ 1.83 = 74.9

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA IF | Nucleoplasm (Approved) | Approved |
| UniProt | No specific annotation in UniProt; HPA Approved | 实验证据 (ECO) |
| GO-CC | C:nucleoplasm (IDA:HPA) | IDA/IMP 等高证据 |

**结论**: PROSER1 定位于细胞核。HPA Approved Nucleoplasm; UniProt lacks specific CC annotation but GO-CC IDA supports nuclear localization。核定位评分 8/10。

#### 3.2 蛋白大小评估

**评价**: 944 aa，稍偏小/偏大但仍在可行范围内 (100–200 或 800–1200 aa)。大小评分 8/10。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 4 |
| PubMed 搜索链接 | [PROSER1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=%22PROSER1%22%5BTitle%2FAbstract%5D) |

**主要研究方向**: OGT-TET2 interactome, transcriptional regulation, DNA demethylation, proline/serine-rich domain function, novel DUF4476 domain characterization

**关键文献**:
1. Ota et al. (2025). "PROSER1 interacts with OGT and TET2 in transcriptional regulation.". *bioRxiv*. (preprint - OGT/TET2 interactome)
2. Delatte et al. (2016). "Transcriptome-wide distribution and function of RNA hydroxymethylcytosine.". *Science*. (TET enzyme context)
3. Wu & Zhang (2017). "TET-mediated active DNA demethylation: mechanism, function and beyond.". *Nat Rev Genet*. (TET biology)
4. Yang et al. (2016). "O-GlcNAc transferase (OGT) as a nutrient sensor.". *Annu Rev Nutr*. (OGT biology)
5. Bauer et al. (2015). "A coordinated phosphorylation cascade integrates multiple inputs to regulate OGT.". *Nat Struct Mol Biol*. (OGT regulation)

**评价**: 极度新颖 (PubMed 4 篇)。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| pLDDT 平均值 | 44.5 |
| pLDDT > 90 (高置信度) | 7.2% |
| pLDDT 70–90 (置信) | 6.9% |
| pLDDT 50–70 (低置信度) | 4.8% |
| pLDDT < 50 (无序) | 81.1% |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PROSER1/PROSER1-PAE.png]]

**评价**: pLDDT=44.5 (low); 81% disordered; no PDB; PubMed≤100 baseline, low structure quality expected for extremely novel protein 三维结构评分 6/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt/InterPro | Domain of unknown function DUF4476 (IPR028011) |
| UniProt/InterPro | Proline and serine-rich protein 1 (IPR042616) |
| Pfam | PF14771 (DUF4476) |

**染色质调控潜力分析**: DUF4476 uncharacterized domain; PROSER1 family; mentioned in OGT/TET2 interactome context; novel domain discovery potential

**评价**: 调控结构域评分 8/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NHLRC3 | 0.683 | 0.059 | no |
| TCF20 | 0.455 | 0.069 | no |
| HIVEP2 | 0.409 | 0.096 | no |
| QSER1 | 0.481 | 0.0 | no |
| NAA16 | 0.404 | 0.0 | no |

**已知复合体成员** (GO Cellular Component):
- No known complex membership

**PPI 互证分析**:
- STRING + IntAct 共同确认: 无
- 仅 STRING 预测: 5 partners
- 仅 IntAct 实验: 0 interactions
- 调控相关比例: see individual annotations above

**评价**: STRING only textmining/co-expression predictions, no experimental evidence; TCF20/HIVEP2 transcriptional regulators identified as potential partners。PPI 评分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 核定位 | HPA + UniProt + GO-CC | Nucleoplasm (Approved) | 一致 |
| 三维结构 | AlphaFold v6 + PDB | pLDDT = 44.5; PDB: None | 单一来源 |
| PPI | STRING | 5 partners | 单一来源 |

**互证加分明细**:
+1 (HPA Approved + GO-CC IDA nucleoplasm confirmed)

**总计**: +1

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: 74.9/100

**核心优势**:
1. 极度新颖 — 新颖性是评分中最重要维度
2. HPA Approved 核定位确认
3. AlphaFold 低-中等预测 (pLDDT=44.5)，新颖蛋白基线

**风险/不确定性**:
1. IF 图像仅限 HPA Selected 预览，建议获取完整多细胞系 IF 数据
2. 无已知复合体归属，PPI 网络需实验验证
3. 功能性研究极度不足 (PubMed=4)，几乎无直接功能研究

**下一步建议**:
- [ ] HPA IF 多细胞系图像验证核定位
- [ ] Co-IP/MS 实验鉴定互作伙伴
- [ ] ChIP-seq 或 CUT&RUN 鉴定染色质结合位点
- [ ] CRISPR 敲除/敲低表型分析
- [ ] AlphaFold-Multimer 预测潜在复合体结构

### 5. 数据来源

- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PROSER1
- Protein Atlas: https://www.proteinatlas.org/search/PROSER1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PROSER1%22%5BTitle%2FAbstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q86XN7
- STRING: https://string-db.org/network/9606.PROSER1
- AlphaFold: https://www.alphafold.ebi.ac.uk/entry/Q86XN7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PROSER1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PROSER1/IF_images/if_selected_medium.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PROSER1/PROSER1-PAE.png]]




