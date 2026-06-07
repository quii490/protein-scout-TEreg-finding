---
type: protein-evaluation
gene: "MAEL"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAEL 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAEL /  |
| 蛋白大小 | 434 aa / 49.2 kDa |
| UniProt ID | [Q96JY0](https://www.uniprot.org/uniprot/Q96JY0) |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus + Cytoplasm (UniProt, 5 PMIDs), Nucleus speckle, GO: chromatin, male ger |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 434 aa, 49.2 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed = 47 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | pLDDT = 72.25, PDB = 1 条目 |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | HMG box domain (PF09011, PF13017), Maelstrom domain |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | No curated UniProt interactions |
| ➕ 互证加分 | — | max +3 | +1 | — |
| **原始总分** |  |  | **123/183** |  |
| **归一化总分** |  |  | **67.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | — | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 UniProt + GO（9项核/染色质注释） | — |
| UniProt | Nucleus + Cytoplasm (UniProt, 5 PMIDs), Nucleus speckle, GO: chromatin, male germ cell nucleus, nucl | Experimental/ECO evidence |

**结论**: Nucleus + Cytoplasm (UniProt, 5 PMIDs), Nucleus speckle, GO: chromatin, male germ cell nucleus, nucleus, XY body (9 GO-CC)

#### 3.2 蛋白大小评估

434 aa (49.2 kDa)，在理想生化实验范围（200-800 aa）内。

**评价**: 大小适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 47 |
| 最早发表年份 | — |
| Chromatin/epigenetics 比例 | — |

**主要研究方向**:
- HMG box DNA-binding domain protein associated with piRNA pathway. Strong chromatin/DNA-binding domain suggests broader regulatory potential beyond piRNA.

**关键文献**:
1. Cheng YS et al. (2023). "The MAEL expression in mitochondria of human spermatozoa." *Andrology*. PMID: 36779514
2. Shi C et al. (2022). "MAEL Augments Cancer Stemness Properties and Resistance to Sorafenib in HCC." *Cancers (Basel)*. PMID: 35740546
3. Li XD et al. (2016). "Overexpression of maelstrom promotes bladder urothelial carcinoma cell aggressiveness by epigenetically downregulating MTSS1 through DNMT3B." *Oncogene*. PMID: 27181205
4. Tao J et al. (2024). "MAEL in human cancers and implications in prognostication." *Aging (Albany NY)*. PMID: 38301040
5. Liu Y et al. (2025). "Genetic and functional analysis reveals novel mutations in meiotic genes." *J Assist Reprod Genet*. PMID: 40442410

**评价**: HMG box DNA-binding domain protein associated with piRNA pathway. Strong chromatin/DNA-binding domain suggests broader regulatory potential beyond piRNA.

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 72.25 |
| 有序区域 (pLDDT>70) 占比 | 62.9% |
| 可用 PDB 条目 | 1 个 (2CTO) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAEL/MAEL-PAE.png]]

**评价**: HMG box: bonafide DNA-binding domain found in chromatin architectural proteins. Recognizes bent/distorted DNA. Direct chromatin/DNA interaction potential.

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | — |
| SMART | — |
| InterPro/Pfam | HMG box domain (PF09011, PF13017), Maelstrom domain |

**染色质调控潜力分析**: HMG box: bonafide DNA-binding domain found in chromatin architectural proteins. Recognizes bent/distorted DNA. Direct chromatin/DNA interaction potential.

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| No curated UniProt interactions | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TDRD9(0.969), PIWIL4(0.957), DDX4(0.925), TDRKH(0.915), PIWIL2(0.913), MOV10L1(0 | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: autosome, chromatin, chromatoid body, cytoplasm, male germ cell nucleus, nucleus, P granule, perinuclear region, piP-body, XY body (10 terms)

**IntAct 查询记录**: IntAct 查询无物理互作记录. STRING 显示 piRNA 通路高置信度功能关联

**PPI 互证分析**:
- STRING + IntAct 共同确认: —
- 仅 STRING 预测: —
- 仅 IntAct 实验: —
- 调控相关比例: — / — (— %)

**评价**: HMG box DNA-binding domain protein associated with piRNA pathway. Strong chromatin/DNA-binding domain suggests broader regulatory potential beyond piRNA.

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=72.25, PDB=1条目 | — |
| 结构域 | UniProt / InterPro / Pfam | HMG box domain (PF09011, PF13017), Maelstrom domain | — |
| PPI | STRING + IntAct | — | — |
| 定位 | Protein Atlas / UniProt / GO | Nucleus + Cytoplasm (UniProt, 5 PMIDs), Nucleus speckle, GO: | — |

**互证加分明细**:
- —
**总分**: +1 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. HMG box domain = bona fide chromatin/DNA-binding
2. Strong literature-supported nuclear localization (5+ PMIDs)
3. Relatively understudied (PubMed=47)
4. 10 GO-CC terms with chromatin/nuclear annotations

**风险/不确定性**:
1. Mainly studied in germ cells
2. AlphaFold moderate (pLDDT 72.3)
3. Nuclear+cytoplasmic shuttling
4. PPI mostly piRNA pathway

**下一步建议**:
- [ ] HPA IF 实验验证核定位
- [ ] Co-IP 验证 PPI
- [ ] 功能实验验证染色质调控角色

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q96JY0
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JY0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAEL%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/Q96JY0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MAEL-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MAEL/MAEL-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96JY0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR024970;IPR039259; |
| Pfam | PF09011;PF13017; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143194-MAEL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX39A | Biogrid | false |
| EIF3F | Biogrid | false |
| EIF4A1 | Biogrid | false |
| ELAVL1 | Biogrid | false |
| KHSRP | Biogrid | false |
| NUDC | Biogrid | false |
| PABPC1 | Biogrid | false |
| SYNCRIP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
