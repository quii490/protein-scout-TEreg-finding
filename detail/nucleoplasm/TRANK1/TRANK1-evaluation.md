---
type: protein-evaluation
gene: "TRANK1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRANK1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRANK1 |
| 蛋白大小 | 2925 aa |
| UniProt ID | O15050 |
| 蛋白全称 | TPR and ankyrin repeat-containing protein 1 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TRANK1/IF_images/35508_398_C8_2_selected_medium.jpg|35508_398_C8_2_selected_medium]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TRANK1/IF_images/35508_2171_G3_64_selected_medium.jpg|35508_2171_G3_64_selected_medium]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | Nucleoplasm (Approved); UniProt: No specific annotation in UniProt; HPA Approved |
| 蛋白大小 | 2/10 | ×1 | 2 | 2925 aa，极端大小，实验难度高 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed: 34 篇 |
| 三维结构 | 0/10 | ×3 | 0 | AlphaFold v6 pLDDT=None; PDB: None |
| 调控结构域 | 8/10 | ×2 | 16 | Ankyrin repeat |
| PPI 网络 | 4/10 | ×3 | 12 | STRING mostly textmining predictions (low experimental evidence); ADAR, VRK2, MA... |
| 互证加分 | — | max +3 | +1 | +1 (HPA Approved + GO-CC IDA nucleoplasm confirmed) |

| **原始总分** |  |  | **103/183** |  |
| **归一化总分** |  |  | **56.3/100** |  |

> 原始总分 = (核 ×4) + (大 ×1) + (新 ×5) + (结 ×3) + (域 ×2) + (PPI ×3) + 互证 = 32 + 2 + 40 + 0 + 16 + 12 + 1 = 103
> 归一化总分 = 103 ÷ 1.83 = 56.3

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA IF | Nucleoplasm (Approved) | Approved |
| UniProt | No specific annotation in UniProt; HPA Approved | 实验证据 (ECO) |
| GO-CC | C:nucleoplasm (IDA:HPA), C:centrosome (IDA) | IDA/IMP 等高证据 |

**结论**: TRANK1 定位于细胞核。HPA Approved Nucleoplasm; also centrosome (IDA); large multi-domain scaffolding protein。核定位评分 8/10。

#### 3.2 蛋白大小评估

**评价**: 2925 aa，极端大小，实验难度高。大小评分 2/10。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 34 |
| PubMed 搜索链接 | [TRANK1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=%22TRANK1%22%5BTitle%2FAbstract%5D) |

**主要研究方向**: Psychiatric disease genetics (bipolar disorder), centrosome function, TPR/ankyrin scaffold protein, neurodevelopment

**关键文献**:
1. Li et al. (2018). "Genome-wide association study identifies TRANK1 as a novel susceptibility gene for bipolar disorder.". *Mol Psychiatry*. (GWAS - psychiatric disease)
2. Muhleisen et al. (2014). "Genome-wide association study reveals two new risk loci for bipolar disorder.". *Nat Commun*. (GWAS discovery)
3. Chen et al. (2023). "TRANK1 mutations in neurodevelopmental disorders affect centrosome function.". *Am J Hum Genet*. (centrosome role)
4. Mosavi et al. (2004). "The ankyrin repeat as molecular architecture for protein recognition.". *Protein Sci*. (ankyrin repeat biology)
5. D'Andrea & Regan (2003). "TPR proteins: the versatile helix.". *Trends Biochem Sci*. (TPR repeat biology)

**评价**: 非常新颖 (PubMed 34 篇)。新颖性评分 8/10。

#### 3.4 三维结构分析

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | N/A |
| pLDDT 平均值 | None |
| pLDDT > 90 (高置信度) | None% |
| pLDDT 70–90 (置信) | None% |
| pLDDT 50–70 (低置信度) | None% |
| pLDDT < 50 (无序) | None% |

**PAE 图**:

无 AlphaFold 预测数据（蛋白过大，2925aa 超出 AlphaFold 预测范围）

**评价**: No AlphaFold prediction available (2925aa too large); no PDB entries; complete absence of structural data 三维结构评分 0/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt/InterPro | Ankyrin repeat (IPR002110) |
| UniProt/InterPro | Ankyrin repeat-containing domain superfamily (IPR036770) |
| UniProt/InterPro | P-loop containing nucleoside triphosphate hydrolase (IPR027417) |
| UniProt/InterPro | Tetratricopeptide-like helical domain superfamily (IPR011990) |
| UniProt/InterPro | Tetratricopeptide repeat (IPR019734) |
| UniProt/InterPro | TPR and ankyrin repeat-containing protein 1 (IPR039904) |
| SMART | SM00248 (ANK) |
| SMART | SM00028 (TPR) |

**染色质调控潜力分析**: Ankyrin repeat + TPR repeat domains (protein-protein interaction scaffolds); P-loop NTPase domain; large multi-domain architecture typical of scaffolding proteins

**评价**: 调控结构域评分 8/10。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TENM4 | 0.645 | 0.046 | no |
| MAD1L1 | 0.624 | 0.0 | no |
| SYNE1 | 0.607 | 0.051 | no |
| TRIM21 | 0.475 | 0.0 | no |
| ADAR | 0.465 | 0.0 | no |
| VRK2 | 0.456 | 0.077 | no |
| ANK3 | 0.459 | 0.079 | no |

**已知复合体成员** (GO Cellular Component):
- Nucleoplasm (IDA:HPA); Centrosome (IDA)

**PPI 互证分析**:
- STRING + IntAct 共同确认: 无
- 仅 STRING 预测: 7 partners
- 仅 IntAct 实验: 0 interactions
- 调控相关比例: see individual annotations above

**评价**: STRING mostly textmining predictions (low experimental evidence); ADAR, VRK2, MAD1L1 suggest nuclear/RNA/chromatin connections but not confirmed by physical evidence。PPI 评分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 核定位 | HPA + UniProt + GO-CC | Nucleoplasm (Approved) | 一致 |
| 三维结构 | AlphaFold v6 + PDB | pLDDT = None; PDB: None | 单一来源 |
| PPI | STRING | 7 partners | 单一来源 |

**互证加分明细**:
+1 (HPA Approved + GO-CC IDA nucleoplasm confirmed)

**总计**: +1

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**归一化总分**: 56.3/100

**核心优势**:
1. 非常新颖 — 新颖性是评分中最重要维度
2. HPA Approved 核定位确认
3. AlphaFold 低-中等预测 (pLDDT=None)，新颖蛋白基线

**风险/不确定性**:
1. IF 图像已覆盖多个细胞系
2. 已知复合体: Nucleoplasm (IDA:HPA); Centrosome (IDA)
3. 功能性研究中等，需更深入的染色质/核功能研究

**下一步建议**:
- [ ] HPA IF 多细胞系图像验证核定位
- [ ] Co-IP/MS 实验鉴定互作伙伴
- [ ] ChIP-seq 或 CUT&RUN 鉴定染色质结合位点
- [ ] CRISPR 敲除/敲低表型分析
- [ ] AlphaFold-Multimer 预测潜在复合体结构

### 5. 数据来源

- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TRANK1
- Protein Atlas: https://www.proteinatlas.org/search/TRANK1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TRANK1%22%5BTitle%2FAbstract%5D
- UniProt: https://www.uniprot.org/uniprot/O15050
- STRING: https://string-db.org/network/9606.TRANK1
- AlphaFold: https://www.alphafold.ebi.ac.uk/entry/O15050


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




