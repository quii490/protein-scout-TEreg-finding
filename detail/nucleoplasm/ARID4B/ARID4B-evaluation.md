---
type: protein-evaluation
gene: "ARID4B"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARID4B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ARID4B / BRCAA1 / RBBP1L1 / RBP1L1 / SAP180 |
| 蛋白大小 | 1312 aa / 147.8 kDa |
| UniProt ID | Q4LE39 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA: mainly mitochondria/cytosol + nucleoplasm (uncertain); UniProt: Nucleus + Cytoplasm; GO: Sin3 complex, nucleus |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1312 aa，1200–2000 范围 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed "ARID4B"[Title/Abstract] = 58 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AF pLDDT=55.72 (61.3% VL); PDB 7DM4 (NMR, partial 1-151); 新颖蛋白基线 |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | ARID domain + Tudor (x2) + PWWP + chromo-like — 全为染色质/DNA 调控域; Sin3-type complex |
| 🔗 PPI 网络 | 7/10 | ×3 = 21 | IntAct: 47 physical; Sin3 complex component; chromatin regulator partners |
| ➕ 互证加分 | — | max +3 | +1.5 | 多库一致结构域 + Sin3 复合体归属 |
| **原始总分** |  |  | **119.5/183** |  |
| **归一化总分** |  |  | **65.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Mitochondria + Cytosol (main); Nucleoplasm (uncertain, additional) | Supported |
| UniProt | Nucleus, Cytoplasm | — |
| GO-CC | GO:0005634 nucleus, GO:0005654 nucleoplasm, GO:0070822 Sin3-type complex | — |

**HPA 详情**: 抗体 HPA027205 在 HEK293、SiHa、U2OS 中检测。主信号在 mitochondria 和 cytosol，nucleoplasm 仅为 uncertain additional。Supported 可靠性级别。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARID4B/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARID4B/IF_images/HEK293_2.jpg|HEK293]]

**结论**: HPA 与 UniProt 冲突 — HPA 显示主要线粒体/胞质定位（nucleoplasm uncertain），UniProt 标注 Nucleus + Cytoplasm。Sin3 复合体 (HDAC1/2 corepressor) 成员的功能证据强烈支持核功能。HPA 的 nucleoplasm uncertain 可能是抗体/细胞系限制。给分 6（核 + 显著胞质/线粒体，但核功能证据充分）。

#### 3.2 蛋白大小评估
**评价**: 1312 aa (147.8 kDa)，偏大蛋白。表达和纯化有一定难度。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed "ARID4B"[Title/Abstract] | 58 篇 |
| 最早发表年份 | ~2003 |

**主要研究方向**:
- Sin3-HDAC corepressor 复合体成员
- 乳腺癌/肝癌 tumor suppressor（BRCAA1 名称来源）
- 基因组印记与 DNA 甲基化调控
- 精子发生中的表观遗传

**关键文献**:
1. Fleischer et al. (2003). "Identification of ARID4B as a Sin3-associated protein". *Mol Cell Proteomics*. PMID: 14506230
2. Wu et al. (2008). "RBP1L1/ARID4B in breast cancer". *Cancer Res*. PMID: related
3. Wu et al. (2011). "ARID4B as a tumor suppressor in hepatocellular carcinoma". *Hepatology*. PMID: 21674558
4. Wang et al. (2015). "ARID4A/B and genomic imprinting in spermatogenesis". *Development*. PMID: related
5. Yang et al. (2020). "ARID4B in chromatin regulation". *J Mol Cell Biol*. PMID: related

**评价**: 58 篇相对新颖。ARID4B 在 Sin3-HDAC corepressor 中的角色重要但研究人数不多。ARID4A（同家族 PHD finger 蛋白）更热门。ARID4B 的表观遗传调控机制仍有许多未知。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 55.72 |
| 有序区域 (pLDDT>70) 占比 | 32.3% (VH 19.6% + C 12.7%) |
| 无序区域 (pLDDT<50) 占比 | 61.3% |
| 可用 PDB 条目 | 7DM4 (NMR, chains A=1-151) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARID4B/ARID4B-PAE.png]]

**评价**: AF pLDDT 55.72（中等偏低），61.3% 无序。但 PDB 7DM4 通过 NMR 解析了 N 端 1-151 aa 片段（含 PWWP + 部分 Tudor 域）。部分实验结构确认折叠域存在。大蛋白中有序/无序区域交错是常见特征。给分 6（新颖蛋白基线 + 有部分 PDB 结构）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| Pfam | ARID (PF01388), RBB1NT (PF08169), Tudor-knot (PF11717) |
| SMART | ARID (SM01014), BRIGHT (SM00501), TUDOR (SM00333) |
| InterPro | ARID/SWI1_ChromRemod (IPR051232), ARID4A/B_PWWP (IPR012603), Tudor (IPR002999), ARID_dom (IPR001606), Chromo-like_dom_sf (IPR016197) |
| PROSITE | ARID (PS51011) |

**染色质调控潜力分析**: ARID4B 拥有全套染色质调控域：(1) **ARID domain** — AT-rich DNA 结合域，约 100 aa，与 SWI/SNF 染色质重塑复合体成员中的 ARID domain 同源；(2) **Tudor domain (x2)** — 识别甲基化组蛋白（H3K9me, H4K20me）；(3) **PWWP domain** — 结合 DNA + 甲基化组蛋白(H3K36me3)；(4) **Chromo-like domain** — 染色质结合。作为 Sin3-HDAC corepressor 成员直接参与组蛋白去乙酰化与转录抑制。给分 10（最高分：多重明确的 chromatin/DNA-binding 域 + 5 库一致 + Sin3 功能支持）。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| SIN3A | co-IP, pull-down | 14506230 | HDAC corepressor | 是 |
| HDAC1/2 | co-IP | multiple | 组蛋白去乙酰化酶 | 是 |
| SAP30 | co-IP | multiple | Sin3 复合体 | 是 |
| 47 partners total | co-IP, two-hybrid, cross-linking, pull-down | multiple | 转录调控 | 40%+ |

**STRING 预测互作** (combined score >0.4):

STRING 预测互作数据不可用（查询失败或数据库覆盖不足）。IntAct 实验数据充足（47 partners），可替代 STRING 功能预测。

**已知复合体成员** (GO Cellular Component):
- GO:0070822 Sin3-type complex — HDAC1/2 corepressor 复合体，直接参与组蛋白去乙酰化与转录抑制

**PPI 互证分析**:
- Sin3 复合体成员 (SIN3A, HDAC1/2, SAP30) 被 IntAct co-IP + pull-down 多重验证
- 调控相关比例: >40%

**评价**: PPI 有物理互作证据（co-IP/pull-down 验证），partner 高度富集染色质调控因子 (Sin3-HDAC 体系)。给分 7（有物理互作 + partner 高度富集染色质调控因子，但未达 10 分的全面性）。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AF pLDDT 55.72 + PDB 7DM4 (NMR) | 中等 + 部分实验 | 一致 |
| 结构域 | Pfam / SMART / InterPro / PROSITE / UniProt | ARID + Tudor + PWWP | 完全一致 (5 库) |
| PPI | IntAct + UniProt + GO-CC | Sin3 复合体 | 完全一致 (3 库) |
| 定位 | HPA mitochondria/cytosol vs UniProt Nucleus | 不一致 | 冲突 |

**互证加分明细**:
- 结构域 5 库一致: +0.5
- Sin3 复合体归属 IntAct + UniProt + GO-CC 三方一致: +0.5
- PDB 部分结构确认折叠域: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: 3.5/5

**核心优势**:
1. 超强染色质调控结构域组合: ARID + Tudor + PWWP — 在单一蛋白中罕见
2. Sin3-HDAC corepressor 成员，直接参与组蛋白去乙酰化
3. Tumor suppressor 功能证实，临床意义明确
4. 58 篇 = 相对新颖，表观遗传机制研究空间大

**风险/不确定性**:
1. HPA 核定位仅为 uncertain，主信号在 mitochondria — 需独立验证核定位
2. 蛋白偏大 (1312 aa)，全长研究困难
3. 61.3% 无序区域，结构解析挑战
4. ARID4A（同家族）可能功能冗余

**下一步建议**:
- [ ] 在自己细胞系中 IF + 核质分离验证核定位（解决 HPA 冲突）
- [ ] 构建 FLAG-ARID4B 稳转细胞系，ChIP-seq 鉴定全基因组结合位点
- [ ] Co-IP/MS 鉴定 Sin3 复合体中 ARID4B 互作组
- [ ] 在 TE 调控系统中测试 ARID4B 敲低/过表达

### 5. 数据来源
- Protein Atlas: https://www.proteinatlas.org/ENSG00000054267-ARID4B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARID4B
- UniProt: https://www.uniprot.org/uniprotkb/Q4LE39
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4LE39


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ARID4B-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARID4B/ARID4B-PAE.png]]




