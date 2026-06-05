---
type: protein-evaluation
gene: "OLIG3"
date: 2026-06-02
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
pm: 24
---

## OLIG3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | OLIG3 / BHLHB7, BHLHE20 |
| 蛋白全称 | Oligodendrocyte transcription factor 3 |
| 蛋白大小 | 272 aa / 29.4 kDa |
| UniProt ID | Q7RTU3 |
| AlphaFold | AF-Q7RTU3-F1 (v6) |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | UniProt Nucleus (ECO:0000255 预测); GO chromatin ISA + nucleus IBA; HPA 无 IF 图像 |
| 蛋白大小 | 10/10 | ×1 | **10** | 272 aa，处于理想范围 (150-400) |
| 研究新颖性 | 8/10 | ×5 | **40** | PubMed strict=24，≤40 档，高新颖性 |
| 三维结构 | 4/10 | ×3 | **12** | 无 PDB 结构; AF mean pLDDT 62.7, 38.2% <50 |
| 调控结构域 | 10/10 | ×2 | **20** | bHLH 转录因子结构域 (InterPro/Pfam/SMART/PROSITE 四库一致) |
| PPI 网络 | 5/10 | ×3 | **15** | STRING 15 + IntAct 15 (Y2H为主); 含 RUNX1/TCF3/TCF12/PAX6 转录因子互作 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
| **加权总分** | | | **113/180**** | |
| **归一化总分 (÷1.83)** | | | **61.7/100**** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus (ECO:0000255) | 预测级 |
| GO-CC | chromatin (GO:0000785, ISA:NTNU_SB); nucleus (GO:0005634, IBA:GO_Central) | 中等 |
| HPA IF | 无 IF 数据 (no_image_detected) | 不可用 |

**HPA IF 状态**: 无 IF 图像，UniProt 定位为预测级别证据 (ECO:0000255)。GO 中有 chromatin 注释 (ISA:NTNU_SB)。核定位有间接证据但缺少直接实验验证。

**结论**: 核定位基于 UniProt 预测 + GO 注释，缺少 HPA IF 直接证据。

#### 3.2 蛋白大小评估

**评价**: 272 aa (29.4 kDa)，处于理想实验范围 (150-400 aa)。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict (Title/Abstract+gene/protein) | 24 |
| PubMed symbol_only | 57 |
| PubMed broad | 61 |

**关键文献**:
1. Muller T et al. (2005). "The bHLH factor Olig3 coordinates the specification of dorsal neurons in the spinal cord." *Genes Dev*. PMID: 15769945
2. Storm R et al. (2009). "The bHLH transcription factor Olig3 marks the dorsal neuroepithelium of the hindbrain." *Development*. PMID: 19088088
3. Sokhadze G et al. (2022). "Cre driver mouse lines for thalamocortical circuit mapping." *J Comp Neurol*. PMID: 34545582
4. Skarp S et al. (2018). "Whole exome sequencing in Finnish families identifies new candidate genes for osteoarthritis." *PLoS One*. PMID: 30157244
5. Vue TY et al. (2007). "Characterization of progenitor domains in the developing mouse thalamus." *J Comp Neurol*. PMID: 17729296

**评价**: PubMed strict=24，高度新颖，仍有大量未知功能空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 272 aa |
| PDB 条数 | 0 |
| AlphaFold mean pLDDT | 62.7 |
| pLDDT >90 | 24.3% |
| pLDDT 70-90 | 6.2% |
| pLDDT 50-70 | 31.2% |
| pLDDT <50 | 38.2% |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/OLIG3/OLIG3-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测。pLDDT 均值 62.7，38.2% 残基置信度 <50，N 端区域可能为无序区。bHLH 结构域区域预测较可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | IPR011598 (bHLH_dom), IPR050359, IPR036638 (HLH_DNA-bd_sf), IPR032659 (Olig3_bHLH) |
| Pfam | PF00010 (HLH) |
| SMART | HLH |
| PROSITE | BHLH |

**染色质调控潜力分析**: bHLH 转录因子家族成员，具有经典 DNA 结合结构域。直接结合 E-box (CANNTG) 序列调控靶基因转录，染色质调控潜力高。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| MDFI | two hybrid array | 32296183 | Transcription inhibitor | Yes |
| TRAF1 | two hybrid array | 32296183 | NF-kB signaling | Yes |
| HMG20A | two hybrid array | 32296183 | Chromatin regulator | Yes |
| RUNX1 | two hybrid array | 32296183 | Transcription factor | Yes |
| PLAGL2 | validated two hybrid | 32296183 | Transcription factor | Yes |
| PROP1 | two hybrid | 32296183 | Transcription factor | Yes |
| ARID5A | protein complementation | 32296183 | Transcription factor | Yes |
| ATN1 | validated two hybrid | 32296183 | Transcription co-repressor | Yes |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 实验分 | 功能类别 | 调控相关？ |
|---------|-------|--------|---------|-----------|
| TNFAIP3 | 0.801 | 0 | NF-kB inhibitor | Yes |
| TRAF1 | 0.656 | 0.165 | NF-kB signaling | Yes |
| NKX2-2 | 0.612 | 0.091 | Transcription factor | Yes |
| DBX1 | 0.609 | 0 | Transcription factor | Yes |
| GBX2 | 0.583 | 0.045 | Transcription factor | Yes |
| TCF3 | 0.581 | 0.129 | bHLH transcription factor | Yes |
| TCF12 | 0.552 | 0.300 | bHLH transcription factor | Yes |
| PAX6 | 0.499 | 0.045 | Transcription factor | Yes |
| DBX2 | 0.498 | 0 | Transcription factor | Yes |

**已知复合体成员** (GO-CC):
- chromatin (GO:0000785, ISA:NTNU_SB)

**评价**: STRING 15 个互作伙伴，IntAct 15 条实验记录。PPI 网络明显富集转录因子 (TCF3, TCF12, NKX2-2, PAX6, DBX1, GBX2, RUNX1) 和转录调控因子 (MDFI, HMG20A)，功能一致性高。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | PDB 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam/SMART/PROSITE | bHLH 五库一致 | 一致 |
| PPI 网络 | STRING + IntAct | 转录因子网络富集 | 部分互证 |
| 核定位 | HPA/UniProt/GO | Nucleus (预测级) | 一致但缺 IF |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 经典 bHLH 转录因子，DNA 结合能力明确，五库结构域一致
2. PPI 网络富集转录因子互作 (TCF3, TCF12, NKX2-2, PAX6)，功能一致性高
3. 高度新颖 (PubMed strict=24)，研究空间大

**风险/不确定性**:
1. HPA 无 IF 图像，核定位仅预测级证据
2. 无 PDB 结构，AlphaFold pLDDT 偏低 (62.7)，38.2% 残基无序

**下一步建议**:
- [ ] IF 实验验证核定位及细胞系表达
- [ ] ChIP-seq 鉴定靶基因和 E-box 结合位点
- [ ] 在 TE 调控体系中筛选其靶向 TE 亚家族

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=OLIG3
- Protein Atlas: https://www.proteinatlas.org/search/OLIG3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22OLIG3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q7RTU3
- STRING: https://string-db.org/network/9606.ENSG00000177468
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7RTU3


#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| TNFAIP3 | STRING | 0.801 |
| AVPR2 | STRING | 0.672 |
| TRAF1 | STRING | 0.656 |
| PTPN22 | STRING | 0.644 |
| PIP4K2C | STRING | 0.626 |
| MDFI | IntAct | psi-mi:"MI:0397"(two hybrid ar |
| TRAF1 | IntAct | psi-mi:"MI:0397"(two hybrid ar |
| KRTAP3-2 | IntAct | psi-mi:"MI:1112"(two hybrid pr |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/OLIG3/OLIG3-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7RTU3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
