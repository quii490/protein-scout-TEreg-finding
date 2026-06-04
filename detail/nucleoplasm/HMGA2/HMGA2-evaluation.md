---
type: protein-evaluation
gene: "HMGA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HMGA2 — REJECTED (研究热度过高 (PubMed strict=1286，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HMGA2 / HMGIC |
| 蛋白名称 | High mobility group protein HMGI-C |
| 蛋白大小 | 109 aa / 11.8 kDa |
| UniProt ID | P52926 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli, Nucleoli rim; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 109 aa / 11.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1286 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017956, IPR000116, IPR000637; Pfam: PF02178 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Nucleoli rim | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- male germ cell nucleus (GO:0001673)
- nuclear chromosome (GO:0000228)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)
- senescence-associated heterochromatin focus (GO:0035985)
- SMAD protein complex (GO:0071141)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1286 |
| PubMed broad count | 2093 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HMGIC |

**关键文献**:
1. HMGA2 facilitates colorectal cancer progression via STAT3-mediated tumor-associated macrophage recruitment.. *Theranostics*. PMID: 34976223
2. HMGA2 and protein leucine methylation drive pancreatic cancer lineage plasticity.. *Nature communications*. PMID: 40419509
3. HMGA2 directly mediates chromatin condensation in association with neuronal fate regulation.. *Nature communications*. PMID: 37828010
4. Genomic landscape of endometrial polyps.. *Genome medicine*. PMID: 41137179
5. Beneath HMGA2 alterations in pleomorphic adenomas: Pathological, immunohistochemical, and molecular insights.. *Human pathology*. PMID: 39089476

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 36.7% |
| 中等置信 (pLDDT 50-70) 占比 | 49.5% |
| 低置信 (pLDDT<50) 占比 | 13.8% |
| 有序区域 (pLDDT>70) 占比 | 36.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 36.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017956, IPR000116, IPR000637; Pfam: PF02178 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IGF2BP2 | 0.996 | 0.000 | — |
| SMAD3 | 0.963 | 0.091 | — |
| SMAD2 | 0.941 | 0.095 | — |
| SMAD4 | 0.936 | 0.045 | — |
| IGF2BP3 | 0.909 | 0.292 | — |
| HMGA1 | 0.902 | 0.000 | — |
| TP53 | 0.867 | 0.292 | — |
| COX6C | 0.858 | 0.000 | — |
| SMAD5 | 0.840 | 0.294 | — |
| IGF2BP1 | 0.840 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRMT6 | psi-mi:"MI:0047"(far western blotting) | imex:IM-14484|pubmed:16293633 |
| PRMT1 | psi-mi:"MI:0516"(methyltransferase radiometric ass | imex:IM-14484|pubmed:16293633 |
| Rb1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11861|pubmed:16766265 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| DLST | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SYDE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ATM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-23312|pubmed:26045162 |
| H2AX | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-23312|pubmed:26045162 |
| Psmb3 | psi-mi:"MI:0096"(pull down) | imex:IM-23312|pubmed:26045162 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 无 | pLDDT=64.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli, Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HMGA2 — High mobility group protein HMGI-C，研究基础较多，新颖性有限。
2. 蛋白大小109 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1286 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1286 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52926
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149948-HMGA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HMGA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52926
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
