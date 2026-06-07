---
type: protein-evaluation
gene: "ANKRD52"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation, ]
status: scored
---

## ANKRD52 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ANKRD52（无别名） |
| 蛋白大小 | 1076 aa / 115.1 kDa |
| UniProt ID | Q8NB46 (Swiss-Prot) |
| 评估日期 | 2026-05-28 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD52/IF_images/A431_1.jpg|A431_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD52/IF_images/U2OS_1.jpg|U2OS_1]]

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | **16** | Protein Atlas: Nucleoplasm+Mitochondria(Approved); 核-线粒体双定位 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 1076 aa / 115.1 kDa, 800-1200 aa范围 |
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed 20篇; 极度新颖; PP6磷酸酶复合体 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | AF pLDDT 85.6; 69.4%>90; 无PDB; 新颖基线5+AF高质量→8 |
| 🧬 调控结构域 | 6/10 | ×2 | **12** | 28xANK repeats(蛋白互作域); 新颖基线6 |
| 🔗 PPI | 3/10 | ×3 | **9** | PPP6C(0.973),PPP6R2(0.943),SIRT7(0.670); 20-25%调控相关→3 |
| ➕ 互证加分 | — | — | **+0.5** | 定位单源 |
| **原始总分** |  |  | **119.5/183** |  |
| **归一化总分** |  |  | **65.3/100** |  |

#### 3.6 PPI 网络（四源综合）

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| hsa-miR-744-5p | CLASH | 23622248 | microRNA | ❌ (非蛋白) |
| hsa-miR-339-5p | CLASH | 23622248 | microRNA | ❌ |
| hsa-miR-331-3p | CLASH | 23622248 | microRNA | ❌ |
| hsa-miR-27b-3p | CLASH | 23622248 | microRNA | ❌ |
| hsa-let-7b-5p | CLASH | 23622248 | microRNA | ❌ |
| hsa-miR-92b-3p | CLASH | 23622248 | microRNA | ❌ |
| hsa-miR-877-3p | CLASH | 23622248 | microRNA | ❌ |
| hsa-miR-766-3p | CLASH | 23622248 | microRNA | ❌ |
| hsa-miR-664a-5p | CLASH | 23622248 | microRNA | ❌ |

> IntAct 中 ANKRD52 的实验互作全部为 miRNA CLASH (cross-linking, ligation, and sequencing of hybrids)，无蛋白-蛋白实验互作。这与其 RNA 结合功能的报道一致。

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| PPP6C | 0.973 | PP6 catalytic subunit, phosphatase | ❌ |
| PPP6R1 | 0.951 | PP6 regulatory subunit | ❌ |
| PPP6R2 | 0.943 | PP6 regulatory subunit | ❌ |
| PPP6R3 | 0.763 | PP6 regulatory subunit | ❌ |
| SIRT7 | 0.670 | NAD-dependent deacetylase, chromatin | ✅ |
| ANKRD28 | 0.641 | PP6 regulatory subunit | ❌ |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 染色质/核复合体注释（ANKRD52 的 GO 注释极为稀少）

**PPI 互证分析**:
- IntAct: 仅 miRNA CLASH 数据，无蛋白-蛋白实验互作
- STRING: PP6 磷酸酶全酶组分 (PPP6C + PPP6R1/2/3/ANKRD28)
- 调控相关: SIRT7（NAD+依赖的去乙酰化酶，染色质调控）
- 调控相关比例: 1/6 (16.7%)

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD52/ANKRD52-PAE.png]]

**评价**: 四源增强未改变 ANKRD52 的 PPI 基本情况。IntAct 的实验互作全部为 miRNA CLASH，无蛋白-蛋白互作验证。STRING 仍然以 PP6 磷酸酶全酶为核心网络，SIRT7（染色质去乙酰化酶）是唯一染色质调控关联。GO-CC 无任何核复合体注释。PPI 评分维持 3。

### X. 关键文献 (PubMed)

1. Zhang Y et al. (2013). "Circular intronic long noncoding RNAs.". *Mol Cell*. PMID: 24035497
2. Lee TF et al. (2021). "TAZ negatively regulates the novel tumor suppressor ANKRD52 and promotes PAK1 dephosphorylation in lung adenocarcinomas.". *Biochim Biophys Acta Mol Cell Res*. PMID: 33096142
3. Li X et al. (2021). "Linking circular intronic RNA degradation and function in transcription by RNase H1.". *Sci China Life Sci*. PMID: 34453665
4. Fu Z et al. (2026). "A diagnostic model based on pulmonary microbiota and host gene expression to distinguish colonization from pneumonia.". *Sci Rep*. PMID: 41933095
5. Huang F et al. (2025). "An exploratory study of high-throughput transcriptomic analysis reveals novel mRNA biomarkers for acute myocardial infarction using integrated methods.". *Sci Rep*. PMID: 40069305

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. **极度新颖**（PubMed 20 篇），染色质方向完全空白——如果发现新功能将具突破性
2. **三维结构预测质量极优**（pLDDT 85.6，69% >90），是
3. **PP6 调控亚基**的染色质功能近年才受关注，可能成为新方向切入点
4. **28 个 ANK 重复阵列**暗示广泛的蛋白互作潜能

**风险/不确定性**:
1. **非严格核蛋白**（核+线粒体双定位），且 PP6 已知主要功能在胞质信号通路
2. **无染色质调控的直接证据**，所有染色质推测基于 PP6 全酶功能推演
3. **UniProt 无定位注释**，仅 Protein Atlas 单一来源
4. **PPI - [ ] 检索 ANKRD52 是否在核蛋白质谱数据中出现（BioGRID、AP-MS 数据集）
- [ ] 评估 ANKRD52 在 TE 调控相关的磷酸酶底物中是否出现
- [ ] 尝试获取 humanPPI 数据完善互证

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NB46
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139645-ANKRD52
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NB46
- STRING: https://string-db.org (ANKRD52, species 9606) — 数据获取不稳定
- PubMed: 20 total (ANKRD52[Title/Abstract])
- humanPPI: 


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ANKRD52-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD52/ANKRD52-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NB46 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770;IPR050889; |
| Pfam | PF00023;PF12796;PF13637; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139645-ANKRD52/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HIF1AN | Biogrid, Bioplex | true |
| PPP6C | Biogrid, Opencell, Bioplex | true |
| PPP6R1 | Biogrid, Opencell | true |
| PPP6R2 | Biogrid, Opencell | true |
| PPP6R3 | Biogrid, Opencell | true |
| ANKRD28 | Opencell | false |
| CDK4 | Opencell | false |
| CUL3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
