---
type: protein-evaluation
gene: "EIF3E"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF3E — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3); 研究热度过高 (PubMed strict=122，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF3E |
| 蛋白名称 | Eukaryotic translation initiation factor 3 subunit E |
| 蛋白大小 | 452 aa / 53.0 kDa |
| UniProt ID | A0A7I2V2H9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Nucleus, PML body |
| 蛋白大小 | 10/10 | ×1 | 10 | 452 aa / 53.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=122 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.0/180** | |
| **归一化总分** | | | **33.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus, PML body | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 122 |
| PubMed broad count | 122 |
| 别名(未计入scoring) |  |

**关键文献**:
1. From Initiation to Elongation: eIF3 as a Dual-Phase Guardian of Mitochondrial Integrity and Protein Homeostasis in Skeletal Muscle.. *FASEB J*. PMID: 41989318
2. ALDH2/eIF3E as Novel Regulators of Cardiac Ferroptosis.. *J Cardiovasc Transl Res*. PMID: 41879911
3. Src promotes tumor cell invasion by hijacking the translation machineries.. *Cell Rep*. PMID: 41734063
4. TRIM35 inhibits endometrial cancer progression via ubiquitination and degradation of EIF3E.. *Cell Signal*. PMID: 41429342
5. Domain architecture of plant eukaryotic translation initiation factor 3 subunit E governs interaction with translational cis-elements to regulatepollen tube growth.. *Plant Cell*. PMID: 41701515

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 45.8% |
| 中等置信 (pLDDT 50-70) 占比 | 48.9% |
| 低置信 (pLDDT<50) 占比 | 5.3% |
| 有序区域 (pLDDT>70) 占比 | 45.8% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 45.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF3C | 0.000 | 0.000 | — |
| EIF3J | 0.000 | 0.000 | — |
| EIF3I | 0.000 | 0.000 | — |
| EIF3D | 0.000 | 0.000 | — |
| EIF3F | 0.000 | 0.000 | — |
| EIF3H | 0.000 | 0.000 | — |
| EIF3M | 0.000 | 0.000 | — |
| EIF3G | 0.000 | 0.000 | — |
| EIF3CL | 0.000 | 0.000 | — |
| EIF3K | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P60228 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q14152 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q59EK9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9HC44 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P54257 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q641X8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 无 | pLDDT=67.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, PML body / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF3E — Eukaryotic translation initiation factor 3 subunit E，研究基础较多，新颖性有限。
2. 蛋白大小452 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 122 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A7I2V2H9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104408-EIF3E/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF3E
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A7I2V2H9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
